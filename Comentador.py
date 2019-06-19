import pandas as pd
class Comentador():
    
    try:
        comentarios = pd.read_excel(io="Comentarios.xlsx",sheet_name="Comentarios",index_col=0)
    except:
        print("Falta archivo excel con comentarios")

       
    
    def completar_comentario(self,control,resultado,dato):
        return self.comentarios[resultado][control].format(dato)
        
