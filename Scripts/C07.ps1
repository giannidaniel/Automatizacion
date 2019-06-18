#Obtiene el Path en donde se encuentra el parametro Autodisconnect y lo exporta en un archivo de salida.txt

(Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters -name Autodisconnect).Autodisconnect | Out-File C07.txt -Encoding 'utf8'