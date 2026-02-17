param(
    [ValidateSet("all", "codex", "claude", "opencode")]
    [string]$Agent = "all",

    [ValidateSet("global", "local")]
    [string]$Scope = "global",

    [string]$ProjectRoot = (Get-Location).Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-DirectoryPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PathValue,
        [Parameter(Mandatory = $true)]
        [string]$Label
    )

    if (-not (Test-Path -LiteralPath $PathValue -PathType Container)) {
        throw "$Label not found: $PathValue"
    }
    return (Resolve-Path -LiteralPath $PathValue).Path
}

function Resolve-LatestStableReleaseTag {
    $tags = git ls-remote --refs --tags $script:OfficialReleaseRepoGitUrl "v*" |
        ForEach-Object { ($_ -split "/")[2] } |
        Where-Object { $_ -match "^v\d+\.\d+\.\d+$" }

    if (-not $tags) {
        throw "no stable release tags found in repository: $script:OfficialReleaseRepoGitUrl"
    }

    return $tags |
        Sort-Object { [version]($_.TrimStart("v")) } |
        Select-Object -Last 1
}

function Test-ValidSkillName {
    param(
        [Parameter(Mandatory = $true)]
        [string]$SkillName
    )

    if ($SkillName -eq "." -or $SkillName -eq "..") {
        return $false
    }

    return $SkillName -match "^[A-Za-z0-9._-]+$"
}

$releaseTag = $null
$releaseTempDir = $null
$script:OfficialReleaseRepoGitUrl = "https://github.com/KentoShimizu/sw-agent-skills.git"
$script:OfficialReleaseArchiveBaseUrl = "https://github.com/KentoShimizu/sw-agent-skills"
$managedStateFileName = ".sw-agent-skills-managed"

try {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw "required command not found: git"
    }
    if (-not (Get-Command tar -ErrorAction SilentlyContinue)) {
        throw "required command not found: tar"
    }

    $releaseTag = Resolve-LatestStableReleaseTag

    $releaseTempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("sw-agent-skills-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $releaseTempDir -Force | Out-Null

    $archivePath = Join-Path $releaseTempDir "release.tar.gz"
    $archiveUrl = "$script:OfficialReleaseArchiveBaseUrl/archive/refs/tags/$releaseTag.tar.gz"
    Invoke-WebRequest -Uri $archiveUrl -OutFile $archivePath
    tar -xzf $archivePath -C $releaseTempDir
    if ($LASTEXITCODE -ne 0) {
        throw "failed to extract release archive: $archivePath (exit code: $LASTEXITCODE)"
    }

    $extractedRoot = Get-ChildItem -LiteralPath $releaseTempDir -Directory | Select-Object -First 1
    if (-not $extractedRoot) {
        throw "failed to locate extracted release directory"
    }

    $sourceDirectory = Join-Path $extractedRoot.FullName "skills"
    $sourceResolved = Resolve-DirectoryPath -PathValue $sourceDirectory -Label "source directory"

    if ($Scope -eq "local") {
        $ProjectRoot = Resolve-DirectoryPath -PathValue $ProjectRoot -Label "project root"
    }

    $skillEntries = Get-ChildItem -LiteralPath $sourceResolved -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md") -PathType Leaf }
    if ($skillEntries.Count -eq 0) {
        throw "no skills found under source directory: $sourceResolved"
    }

    $targets = [System.Collections.Generic.List[object]]::new()

    if ($Scope -eq "global") {
        if ($Agent -eq "all" -or $Agent -eq "codex") {
            $targets.Add([pscustomobject]@{ Label = "codex"; Path = (Join-Path $HOME ".codex/skills") })
        }
        if ($Agent -eq "all" -or $Agent -eq "claude") {
            $targets.Add([pscustomobject]@{ Label = "claude"; Path = (Join-Path $HOME ".claude/skills") })
        }
        if ($Agent -eq "all" -or $Agent -eq "opencode") {
            $targets.Add([pscustomobject]@{ Label = "opencode"; Path = (Join-Path $HOME ".config/opencode/skills") })
        }
    } else {
        if ($Agent -eq "all" -or $Agent -eq "codex") {
            $targets.Add([pscustomobject]@{ Label = "codex(local)"; Path = (Join-Path $ProjectRoot ".codex/skills") })
        }
        if ($Agent -eq "all" -or $Agent -eq "claude") {
            $targets.Add([pscustomobject]@{ Label = "claude(local)"; Path = (Join-Path $ProjectRoot ".claude/skills") })
        }
        if ($Agent -eq "all" -or $Agent -eq "opencode") {
            $targets.Add([pscustomobject]@{ Label = "opencode(local)"; Path = (Join-Path $ProjectRoot ".opencode/skills") })
        }
    }

    if ($targets.Count -eq 0) {
        throw "no installation targets resolved"
    }

    Write-Host "release-version: $releaseTag"
    Write-Host "source: $sourceResolved"
    Write-Host "scope: $Scope"

    foreach ($target in $targets) {
        New-Item -ItemType Directory -Force -Path $target.Path | Out-Null
        $managedStatePath = Join-Path $target.Path $managedStateFileName
        $previousManagedSkillNames = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)

        if (Test-Path -LiteralPath $managedStatePath -PathType Leaf) {
            $managedStateLines = Get-Content -LiteralPath $managedStatePath
            foreach ($managedStateLine in $managedStateLines) {
                $managedSkillName = $managedStateLine.Trim()
                if ([string]::IsNullOrWhiteSpace($managedSkillName)) {
                    continue
                }
                if (-not (Test-ValidSkillName -SkillName $managedSkillName)) {
                    throw "invalid managed skill entry in state file: $managedStatePath: $managedSkillName"
                }
                [void]$previousManagedSkillNames.Add($managedSkillName)
            }
        } else {
            foreach ($skillDir in $skillEntries) {
                $legacyDestinationSkillDir = Join-Path $target.Path $skillDir.Name
                if (Test-Path -LiteralPath $legacyDestinationSkillDir) {
                    [void]$previousManagedSkillNames.Add($skillDir.Name)
                }
            }
        }

        foreach ($skillDir in $skillEntries) {
            if (-not (Test-ValidSkillName -SkillName $skillDir.Name)) {
                throw "invalid source skill directory name: $($skillDir.Name)"
            }

            $destinationSkillDir = Join-Path $target.Path $skillDir.Name
            if ((Test-Path -LiteralPath $destinationSkillDir) -and (-not $previousManagedSkillNames.Contains($skillDir.Name))) {
                throw "$($target.Label) target exists and is not managed by installer: $destinationSkillDir"
            }
        }

        foreach ($previousManagedSkillName in $previousManagedSkillNames) {
            $previousManagedSkillDir = Join-Path $target.Path $previousManagedSkillName
            if (Test-Path -LiteralPath $previousManagedSkillDir) {
                Remove-Item -LiteralPath $previousManagedSkillDir -Recurse -Force
            }
        }

        $installedCount = 0
        $currentManagedSkillNames = [System.Collections.Generic.List[string]]::new()
        foreach ($skillDir in $skillEntries) {
            $destinationSkillDir = Join-Path $target.Path $skillDir.Name

            Copy-Item -LiteralPath $skillDir.FullName -Destination $destinationSkillDir -Recurse
            [void]$currentManagedSkillNames.Add($skillDir.Name)
            $installedCount++
        }

        Set-Content -LiteralPath $managedStatePath -Value $currentManagedSkillNames
        Write-Host "installed: $($target.Label) ($($target.Path)) new=$installedCount"
    }

    Write-Host "done."
}
finally {
    if ($releaseTempDir -and (Test-Path -LiteralPath $releaseTempDir)) {
        Remove-Item -LiteralPath $releaseTempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
