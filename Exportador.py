class Exportador():
    
    #Esta Clase trae desde un templete, el listado de ids de conntroles, genera un dataframe con los ids como indices y agrega dos columnas ("comentario" y "resultado") para poder mapear los resultados y controles a analizar

    try:
        matriz = pd.read_excel(io="Matriz.xlsx",sheet_name="Worksheet",index_col=0)
    except:
        print("Falta archivo excel con la matriz")
        
    df=pd.DataFrame(index=matriz.index,columns=["Comentario","Resultado"])
    
    comentador=Comentador()
    
    #Escribe dentro del DataFrame, el comentario y resultado pasado como parametro
    def escribir_resultado(self,control,resultado,dato):

        comentario=self.comentador.completar_comentario(control,resultado,dato)
        
        self.df["Comentario"][control]=comentario
        self.df["Resultado"][control]=resultado
        
    #Exporta el el DataFrame con los resultados y comentarios de lo controles analizados y los exporta a una matriz template
    def guardar_salida(self):
        wb=load_workbook("Matriz.xlsx")
        ws=wb["Worksheet"]
        for fila in self.df.index:
            ws.cell(row=self.matriz.index.get_loc(fila)+2,column=self.matriz.columns.get_loc("Comentario")+2).value=self.df["Comentario"][fila]
            ws.cell(row=self.matriz.index.get_loc(fila)+2,column=self.matriz.columns.get_loc("Resultado")+2).value=self.df["Resultado"][fila] 
        wb.save("Matriz completa.xlsx")