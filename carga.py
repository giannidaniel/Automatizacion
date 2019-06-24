class Carga():
    #Esta funcion pasandole el parametro "ruta" con la ruta del archivo, lo lee y lo guarda en la variable lista (Limitada a archivos con encoding UTF-8)
    def cargador(self,ruta):
        archivo = open(ruta, 'r', encoding = 'utf-8')
        lista = archivo.read()
        archivo.close()
        return lista


    #Esta funcion pasandole el parametro "ruta" con la ruta del archivo, lo lee y lo guarda en la variable lista (Limitada a archivos con encoding UTF-16)        
    def cargador_utf16(self,ruta):
        archivo = open(ruta, 'r', encoding = 'utf-16')
        lista = archivo.read()
        archivo.close()
        return lista