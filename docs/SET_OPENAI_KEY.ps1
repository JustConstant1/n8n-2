param(
    [Parameter(Mandatory = $true)]
    [string]$OpenAIKey
)

$env:OPENAI_API_KEY = $OpenAIKey
Write-Host "OPENAI_API_KEY set for the current PowerShell session."
