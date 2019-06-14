import pandas as pd

class Parser():
    
    def parser_users(self,archivo):
        
    ##Obtiene los encabesados para el data frame
        self.archivo=archivo
        self.archivo=self.archivo.replace("\n\nU","U")[:-3]
        usuario=self.archivo.split("The command completed successfully.")[0]
        encabezado= list(map(lambda x:x[:29].strip(),usuario.split("\n")))
        novacios= list(map(lambda x:x!="",encabezado[:21]))
        encabezado= list(filter(lambda x:x!="",encabezado[:21]))

    ##Obtiene los datos de ada usuario
        usuarios=self.archivo.split("The command completed successfully.")
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
            
    def parser_discos(archivo):
        pass
        
