$server = $env:COMPUTERNAME
GPRESULT /S $server /scope computer /H salida.txt
Get-Content salida.txt | set-content -Encoding utf8 C08_$server.txt
Remove-Item salida.txt
