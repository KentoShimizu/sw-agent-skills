param(
    [ValidateSet("all", "codex", "claude", "opencode")]
    [string]$Agent = "all",

    [ValidateSet("global", "local")]
    [string]$Scope = "global",

    [string]$ProjectRoot = (Get-Location).Path,

    [switch]$Force
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

$releaseTag = $null
$releaseTempDir = $null
$script:OfficialReleaseRepoGitUrl = "https://github.com/KentoShimizu/sw-agent-skills.git"
$script:OfficialReleaseArchiveBaseUrl = "https://github.com/KentoShimizu/sw-agent-skills"

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

        $installedCount = 0

        foreach ($skillDir in $skillEntries) {
            $destinationSkillDir = Join-Path $target.Path $skillDir.Name

            if (Test-Path -LiteralPath $destinationSkillDir) {
                if (-not $Force.IsPresent) {
                    throw "$($target.Label) target exists: $destinationSkillDir (use -Force to replace)"
                }
                Remove-Item -LiteralPath $destinationSkillDir -Recurse -Force
            }

            Copy-Item -LiteralPath $skillDir.FullName -Destination $destinationSkillDir -Recurse

            $installedCount++
        }

        Write-Host "installed: $($target.Label) ($($target.Path)) new=$installedCount"
    }

    Write-Host "done."
}
finally {
    if ($releaseTempDir -and (Test-Path -LiteralPath $releaseTempDir)) {
        Remove-Item -LiteralPath $releaseTempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
