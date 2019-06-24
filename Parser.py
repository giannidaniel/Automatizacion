class Parser():
    
    def parser_users(self,archivo):
    ##Limpia y secciona el listado de usarios del servidor    
    ##Obtiene los encabesados para el data frame
        archivo=archivo.replace("\n\nU","U")
        archivo=archivo.replace("\ufeffU","U")

        usuario=archivo.split("The command completed successfully.")[0]
        encabezado= list(map(lambda x:x[:29].strip(),usuario.split("\n")))
        novacios= list(map(lambda x:x!="",encabezado[:21]))
        encabezado= list(filter(lambda x:x!="",encabezado[:21]))

    ##Obtiene los datos de cada usuario
        usuarios=archivo.split("The command completed successfully.")[:-1]
        datos=[]
        for usuario in usuarios:
            lista=[]
            for i in range(21):
                if novacios[i]:
                    lista.append(usuario.split("\n")[i][29:].strip()) 
            datos.append(lista)
            
    ##Genera y retorna un data frame con los usuarios cargados
        df=pd.DataFrame(data=datos,columns=encabezado)

        return df
    
    def parser_idle(self,archivo):
    #Limpia el archivo de salida del script y lo transforma en un entero
        return int(archivo.replace("\ufeff",""))
        
        

    
    def parser_discos(self,archivo):


        Lista = archivo
        #Separa el archivo en listas por el caracter  "\n".
        Lista = Lista.split('\n')
        #elimina las ultimas lineas.
        Lista.pop()
        Lista.pop()
        Lista.pop()
        Lista.pop(2)
        datoscrudos=Lista[2:]
        datos=[]
        #Delimita las lineas de la 2 en adelante dejando solo el dato sin espacios.
        for linea in datoscrudos:
            datos.append(linea.split())
        #Genera un data frame donde las columnas son la fila 1 de la lista y los datos son todas las lineas de la 2 en adelante.
        df = pd.DataFrame(columns = Lista[1].split(), data = datos) 
        return df
    
    
    def parser_auditlogs(self,archivo):
    	##Divide el archivo por saltos de pagina "\n"
        archi=archivo.split("\n")
        ##Identifica la linea en que comienza el listado de eventos de auditoria ([Event Audit])
        ubicacion=archi.index("[Event Audit]")
        audit=[]
        ##Lee linea por linea agregandolas a la valiarable "audit", hasta que se encuenta una linea con el caracter "[", esto quiere decir, que comineza a listar otras configuraciones de seguridad
        for linea in archi[ubicacion+1:]:
            if "[" in linea:
                break
            audit.append(linea)
        ##Divide y genera un DataFrame con la configuración de los distintos logs de auditoria
        audit=list(map(lambda x:x.split(" = "),audit))
        return pd.DataFrame(index=list(map(lambda x:x[0],audit)),data=list(map(lambda x:x[1],audit)),columns=["Valor"])
        
    def parser_passwords(self,archivo):
        
        flag=0
        data={}
        aux=[]
        ##Esta clase lee todo el archivo html y cuando identifica el comienzo de la politica de passwor y de bloqueo de usuario comienza a agregar la configuración identificada y la retorna
        #Politicas de contraseña de usuario
        for linea in archivo.split("\n"):
            if "Account Policies/Password Policy" in linea:
                flag=1
                continue

            if ("<tr><td>" in linea) and (flag==1):
                aux=linea.replace("<tr><td>","").split("</td><td>")
                data.update({aux[0]:aux[1]})

            if linea=="</table>" and  flag==1:
                break
        flag=0
        
        #Politicas de bloqueo de usuario
        for linea in archivo.split("\n"):
            if "Account Policies/Account Lockout Policy" in linea:
                cunt=1
                continue

            if ("<tr><td>" in linea) and (flag==1):
                aux=linea.replace("<tr><td>","").split("</td><td>")
                data.update({aux[0]:aux[1]})

            if linea=="</table>" and  flag==1:
                break      

        return data
    