import pandas as pd
from openpyxl import load_workbook

#Analisis IDLE
#--------------------------
ana=Analisadora()
resultado,dato=ana.analisis_c07("Idle.txt")
export=Exportador()
export.escribir_resultado("C07",resultado,dato)

#Análisis DISCOS
#--------------------------
disco=Analisis_discos()
resultado,dato=disco.analisis("C06.txt")
export.escribir_resultado("C06",resultado,dato)



export.guardar_salida()