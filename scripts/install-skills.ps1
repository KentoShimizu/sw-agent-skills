param(
    [ValidateSet("all", "codex", "claude", "opencode")]
    [string]$Agent = "all",

    [ValidateSet("global", "local")]
    [string]$Scope = "global",

    [ValidateSet("symlink", "copy")]
    [string]$Mode = "symlink",

    [string]$Source,

    [string]$ProjectRoot = (Get-Location).Path,

    [switch]$DryRun,

    [switch]$VerboseList,

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

function Invoke-InstallAction {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Description,
        [Parameter(Mandatory = $true)]
        [scriptblock]$Action
    )

    if ($DryRun.IsPresent) {
        if ($VerboseList.IsPresent) {
            Write-Host "[dry-run] $Description"
        }
        return
    }
    if ($VerboseList.IsPresent) {
        Write-Host "[run] $Description"
    }
    & $Action
}

function Resolve-SymlinkTarget {
    param(
        [Parameter(Mandatory = $true)]
        [string]$TargetPath
    )

    if (-not (Test-Path -LiteralPath $TargetPath)) {
        return $null
    }

    $item = Get-Item -LiteralPath $TargetPath -Force
    if (-not ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) {
        return $null
    }

    $rawTarget = $item.Target
    if ($rawTarget -is [array]) {
        $rawTarget = $rawTarget[0]
    }
    if (-not $rawTarget) {
        return $null
    }

    $candidate = if ([System.IO.Path]::IsPathRooted($rawTarget)) {
        $rawTarget
    } else {
        Join-Path -Path $item.Directory.FullName -ChildPath $rawTarget
    }

    try {
        return (Resolve-Path -LiteralPath $candidate).Path
    } catch {
        return $null
    }
}

$repoRoot = Split-Path -Parent $PSScriptRoot
if (-not $Source) {
    $Source = Join-Path -Path $repoRoot -ChildPath "skills"
}

$sourceResolved = Resolve-DirectoryPath -PathValue $Source -Label "source directory"
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

Write-Host "source: $sourceResolved"
Write-Host "scope: $Scope"
Write-Host "mode: $Mode"
Write-Host "dry-run: $($DryRun.IsPresent)"
Write-Host "verbose: $($VerboseList.IsPresent)"

foreach ($target in $targets) {
    Invoke-InstallAction -Description "mkdir $($target.Path)" -Action {
        New-Item -ItemType Directory -Force -Path $target.Path | Out-Null
    }

    $installedCount = 0
    $skippedCount = 0

    foreach ($skillDir in $skillEntries) {
        $destinationSkillDir = Join-Path $target.Path $skillDir.Name
        $existingLinkTarget = Resolve-SymlinkTarget -TargetPath $destinationSkillDir
        if ($existingLinkTarget -and $existingLinkTarget -eq $skillDir.FullName) {
            $skippedCount++
            continue
        }

        if (Test-Path -LiteralPath $destinationSkillDir) {
            if (-not $Force.IsPresent) {
                throw "$($target.Label) target exists: $destinationSkillDir (use -Force to replace)"
            }
            Invoke-InstallAction -Description "remove $destinationSkillDir" -Action {
                Remove-Item -LiteralPath $destinationSkillDir -Recurse -Force
            }
        }

        if ($Mode -eq "symlink") {
            Invoke-InstallAction -Description "link $destinationSkillDir -> $($skillDir.FullName)" -Action {
                New-Item -ItemType SymbolicLink -Path $destinationSkillDir -Target $skillDir.FullName | Out-Null
            }
        } else {
            Invoke-InstallAction -Description "copy $($skillDir.FullName) -> $destinationSkillDir" -Action {
                Copy-Item -LiteralPath $skillDir.FullName -Destination $destinationSkillDir -Recurse
            }
        }

        $installedCount++
    }

    Write-Host "installed: $($target.Label) ($($target.Path)) new=$installedCount skipped=$skippedCount"
}

Write-Host "done."
