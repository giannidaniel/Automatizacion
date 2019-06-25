$computer_name = $env:COMPUTERNAME
gwmi Win32_LogicalDisk | select-object -property name,FileSystem,drivetype| Where-Object {$_.drivetype -eq 3 }| Out-File C06_$computer_name.txt -Encoding 'utf8'
