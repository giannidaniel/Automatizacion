class Carga():
    #Esta funcion pasandole el parametro "ruta" con la ruta del archivo, lo lee y lo guarda en la variable lista
    def cargador_utf8(self,ruta):
        self.archivo = open(ruta, 'r', encoding = 'utf-8')
        lista = self.archivo.read()
        self.archivo.close()
        return lista

       #def limpiador():
        
    def cargador_utf16(self,ruta):
        self.ruta=ruta
        self.archivo = open(ruta, 'r', encoding = 'utf-16')
        lista = self.archivo.read()
        self.archivo.close()
        return lista