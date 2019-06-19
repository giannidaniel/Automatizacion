class Analisadora ():

    
    def analisis_c07(self,nombre):
        car = Carga()
        tiempo = car.cargador_utf16(nombre)
        if int(tiempo)<=15:
            resultado="Efectivo"
        else:
            resultado="Inefectivo"
       
        return resultado,int(tiempo)
    
   
    def analisis_c06(self,nombre):
        parser = Parser()
        df= parser.parser_discos(nombre)
        
        
        if df[df['FileSystem']!='NTFS'].empty:
            return "Efectivo",df.to_string(index=False)
        else:
            return "Inefectivo",df[df['FileSystem']!='NTFS'].to_string(index=False)
        