class carga():
    #Esta funcion pasandole el parametro "ruta" con la ruta del archivo, lo lee y lo guarda en la variable lista
    def cargador(self,ruta):
        self.archivo = open(ruta, 'r', encoding = 'utf-8')
        Lista = self.archivo.read()
        self.archivo.close()
        return Lista

       #def limpiador():
        
