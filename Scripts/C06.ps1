#Obtiene la propiedad FileSystem de todos los discos locales (drivetype = 3) y lo exporta a un archivo de salida.txt

gwmi Win32_LogicalDisk | select-object -property name,FileSystem,drivetype| Where-Object {$_.drivetype -eq 3 }| Out-File salida.txt -Encoding 'utf8'