class Comentador():
    
    #Esta Clase trae un templete de comentarios, previamente cargado
    try:
        comentarios = pd.read_excel(io="Comentarios.xlsx",sheet_name="Comentarios",index_col=0)
    except:
        print("Falta archivo excel con comentarios")

       
    #la funicón completar comentario busca en el template de comentarios, el correspondiente al resultado y control que se pase por parametro.
    #Agrega el datos, pasado como parametro, al comentario y lo retorna completo.
    def completar_comentario(self,control,resultado,dato):
        return self.comentarios[resultado][control].format(dato) 