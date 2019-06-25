$server = $env:COMPUTERNAME
GPRESULT /S $server /scope computer /H salida.html
Get-Content salida.html | set-content -Encoding utf8 C08_$server.html
Remove-Item salida.html
