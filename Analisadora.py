class Analisadora():

    
    def analisis_c07(self,tiempo):
        if int(tiempo)<=15:
            resultado="Efectivo"
        else:
            resultado="Inefectivo"
       
        return resultado,int(tiempo)
    
   
    def analisis_c06(self,df):        
        
        if df[df['FileSystem']!='NTFS'].empty:
            return "Efectivo",df.to_string(index=False)
        else:
            return "Inefectivo",df[df['FileSystem']!='NTFS'].to_string(index=False)
        
        
    def analisis_c02(self,usuarios,idioma="Ingles"):
        
             
        def usuario_activo(df,usuario):
            return (df[df["User name"]== usuario]["Account active"]=="Yes").bool()

        def usuario_definido(df,usuario):
            df=df
            usuario=usuario
            return not(df[df["User name"]== usuario].empty)

        
        #Seteo de usuarios a buscar dependiendo del idioma del servidor analizado
        if idioma=="Español":
            admin="Administrador"
            guest="Invitados"
        else:
            admin="Administrator"
            guest="Guest"            
        
        
        resultado="Efectivo"
        activos=""
        
        if usuario_definido(usuarios,admin):
            if usuario_activo(usuarios,admin):
                resultado="Inefectivo"
                activos=activos+admin+"\n"
        if usuario_activo(usuarios,guest):
            resultado="Inefectivo"
            activos=activos+guest+"\n" 

        return resultado,activos        
        
        
    def analisis_c08(self,data):
        obs=[]

        parametro="Enforce password history"

        try:
            data[parametro]
            try:
                if ((int(data[parametro].split(" ")[0]))*int(data["Maximum password age"].split(" ")[0]))<365:
                    resultado="Inefectivo"
                    obs.append([parametro,data[parametro]])      
            except:
                print("Hola")
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Maximum password age"
        try:
            if int(data[parametro].split(" ")[0])>90 :
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]]) 
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Minimum password length"
        try:
            if int(data[parametro].split(" ")[0])<8 :
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]])                        
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Password must meet complexity requirements"
        try:
            if data[parametro]!="Enabled" :
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]]) 
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Store passwords using reversible encryption"    
        try:
            if data[parametro]!= "Disabled":
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]])
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Account lockout threshold"    
        try:
            if not(int(data[parametro].split(" ")[0])<6 and int(data[parametro].split(" ")[0])>1):
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]])
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        parametro="Reset account lockout counter after"    
        try:
            if not(int(data[parametro].split(" ")[0])>=60 or int(data[parametro].split(" ")[0])==0):
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]])
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"


        parametro="Account lockout duration"    
        try:
            if int(data[parametro].split(" ")[0])!= 0:
                resultado="Inefectivo"
                obs.append([parametro,data[parametro]])        
        except:
            obs.append([parametro,"No configurado"])
            resultado="Inefectivo"

        if resultado=="Inefectivo":
            index=list(map(lambda x:x[0],obs))
            data=list(map(lambda x:x[1],obs))
            df=pd.DataFrame(index=index,data=data)
        else:
            df=pd.DataFrame(data)
        
        return resultado,df.to_string(header=False)
        
        
        
        
        
    def analisis_c12(self,df):
        
        #definición de la correcta configuración de los parametros de politicas de auditoria
        audit_ok={'AuditSystemEvents': '2','AuditLogonEvents': '3','AuditObjectAccess': '2','AuditPrivilegeUse': '2','AuditPolicyChange': '3','AuditAccountManage': '3','AuditProcessTracking': '0','AuditDSAccess': '2','AuditAccountLogon': '3'}
        valores={'0':'None','2':'Failure','3':'Success and Failure'}

        resultado="Efectivo"
        
        estado=[]
        valores_traducidos=[]
        
        for linea in df.index:
            
            if (df["Valor"][linea]<audit_ok[linea]):
                estado.append(True)
                resultado="Inefectivo"

            else:
                estado.append(False)
            valores_traducidos.append(valores[df["Valor"][linea]])                             
        
        
        df["Valor_traducido"]=valores_traducidos            
        df["Estado"]=estado 
        datos=df        
        if resultado=="Inefectivo":
            datos=df[df["Estado"]==False]  
 
        return resultado,datos["Valor_traducido"].to_string()
        