class Metadata():
    #Esta clase lee la metadata que se encuentra en el header se los archivos de salida de los scipts
    def leer_idioma(self,archivo):
        for linea in archivo.split("\n"):
            if linea.split(" ")[0]=="Idioma:":
                return linea.split(" ")[1]
        
    
    def leer_servidor(self,archivo):
        for linea in archivo.split("\n"):
            if linea.split(" ")[0]=="Servidor:":
                return linea.split(" ")[1]
    
    
    def leer_control(self,archivo):
        for linea in archivo.split("\n"):
            if linea.split(" ")[0]=="Control:":
                return linea.split(" ")[1]