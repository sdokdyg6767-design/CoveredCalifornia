param(
  [Parameter(Mandatory=$true)][string[]]$Urls,
  [string]$OutDir = ''
)
$ErrorActionPreference = 'Stop'

foreach ($u in $Urls) {
  try {
    $r = Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 60
    $html = $r.Content
  } catch {
    Write-Output "FAILED: $u :: $($_.Exception.Message)"
    continue
  }

  # Next.js payloads embed JSON inside JS string literals, so inner quotes are escaped.
  # Unescape them so the field regexes below can match.
  $html = $html -replace '\\"', '"'

  $out = New-Object System.Collections.Generic.List[string]

  # title / meta description
  if ($html -match '<title>(.*?)</title>') { $out.Add("# TITLE: " + $matches[1]) }

  $patterns = @(
    '"children":"((?:[^"\\]|\\.)*)"',
    '"text":"((?:[^"\\]|\\.)*)"',
    '"description":"((?:[^"\\]|\\.)*)"',
    '"value":"((?:[^"\\]|\\.)*)"',
    '"alt":"((?:[^"\\]|\\.)*)"'
  )

  $seen = New-Object System.Collections.Generic.HashSet[string]
  foreach ($p in $patterns) {
    foreach ($m in [regex]::Matches($html, $p)) {
      $v = $m.Groups[1].Value
      if ([string]::IsNullOrWhiteSpace($v)) { continue }
      try {
        $dec = ('"' + $v + '"' | ConvertFrom-Json)
      } catch { continue }
      $dec = $dec -replace '\u0026','&' -replace '\u003c','<' -replace '\u003e','>' -replace '\n',' '
      $dec = $dec.Trim()
      if ($dec.Length -lt 3) { continue }
      if ($dec -match '^(lucide-|text-|bg-|min-|max-|w-|h-|flex|grid|rounded|body-|label-|display-|heading-|relative|absolute|container|page-|col-|sr-only|inline-|$)') { continue }
      if ($seen.Add($dec)) { $out.Add($dec) }
    }
  }

  Write-Output "===== URL: $u ====="
  $out | ForEach-Object { Write-Output $_ }
  Write-Output ""
}