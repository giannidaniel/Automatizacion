$computer_name = $env:COMPUTERNAME
secedit.exe /export /areas SECURITYPOLICY /cfg filename.txt
Get-Content filename.txt | Set-Content -Encoding utf8 C12_$computer_name.txt
Remove-Item filename.txt
