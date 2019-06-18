import pandas as pd
from carga import *

class Parser():
    
    def parser_users(self,archivo):
        
    ##Obtiene los encabesados para el data frame
        self.archivo=archivo
        self.archivo=self.archivo.replace("\n\nU","U")[:-3]
        usuario=self.archivo.split("The command completed successfully.")[0]
        encabezado= list(map(lambda x:x[:29].strip(),usuario.split("\n")))
        novacios= list(map(lambda x:x!="",encabezado[:21]))
        encabezado= list(filter(lambda x:x!="",encabezado[:21]))

    ##Obtiene los datos de cada usuario
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
            
    def parser_discos(self,archivo):
        #Llamo a la clase carga() para que lea el archivo y lo guarde en una lista.
        cargar = carga()
        Lista = cargar.cargador(archivo)
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
        
