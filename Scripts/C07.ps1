#Obtiene el Path en donde se encuentra el parametro Autodisconnect y lo exporta en un archivo de C07.txt
$computer_name = $env:COMPUTERNAME
(Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters -name Autodisconnect).Autodisconnect | Out-File C07_$computer_name.txt -Encoding 'utf8'
