#!/usr/bin/env pwsh

$prevNodeOptions = $env:NODE_OPTIONS
$env:NODE_OPTIONS='--no-warnings --require "<REPLACE>"'

if ($args) {
  try {
    if ($args.Count -gt 0) {
      $cmd = $args[0]
      $cmdArgs = if ($args.Count -gt 1) { $args[1..($args.Count - 1)] } else { @() }
      & $cmd @cmdArgs
    }
  }
  finally {
    if ($null -ne $prevNodeOptions) {
      $env:NODE_OPTIONS = $prevNodeOptions
    }
    else {
      Remove-Item Env:NODE_OPTIONS -ErrorAction SilentlyContinue
    }
  }
}
