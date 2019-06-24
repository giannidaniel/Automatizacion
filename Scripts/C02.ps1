$computer_name = $env:COMPUTERNAME

$usuarios = @()


$usuarios_locales = get-wmiobject -class win32_useraccount | select-object name


$usuarios_finales = @()

foreach($usuario in $usuarios_locales)
{	
	$usuarios_finales += $usuario.name
}

	

$usuarios += $usuarios_finales | ForEach-Object { cmd.exe /c net user "$_" } 

$usuarios  | Out-File Usuarios.txt -Encoding 'utf8'