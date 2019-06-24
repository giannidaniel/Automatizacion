secedit.exe /export /areas SECURITYPOLICY /cfg filename.txt
Get-Content filename.txt | Set-Content -Encoding utf8 C12.txt
Remove-Item filename.txt