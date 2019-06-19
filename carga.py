class carga():
    #Esta funcion pasandole el parametro "ruta" con la ruta del archivo, lo lee y lo guarda en la variable lista
    def cargador_utf8(self,ruta):
        self.archivo = open(ruta, 'r', encoding = 'utf-8')
        Lista = self.archivo.read()
        self.archivo.close()
        return Lista

       #def limpiador():
        
    def cargador_utf16(self,nombre):
        self.nombre=nombre
        with open(self.nombre,"r",encoding='utf-16') as self.archivo:
        Lista = self.archivo.read()
        self.archivo.close()
        return Lista
