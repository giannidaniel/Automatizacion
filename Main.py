import pandas as pd
from openpyxl import load_workbook
import Analisadora as Analisadora
import Carga as Carga
import Comentador as Comentador
import Exportador as Exportador
import Metadata as Metadata
import Parser as Parser
import Limpiador as Limpiador


#Creación de objetos
#--------------------------
carga=Carga()
ana=Analisadora()
export=Exportador()
parser=Parser()


#Analisis Idle
#--------------------------
archivo=carga.cargador("C07.txt")
arch_parseado=parser.parser_idle(archivo)
resultado,dato=ana.analisis_c07(arch_parseado)
export.escribir_resultado("C07",resultado,dato)

#Analisis Discos
#--------------------------
archivo=carga.cargador("C06.txt")
arch_parseado=parser.parser_discos(archivo)
resultado,dato=ana.analisis_c06(arch_parseado)
export.escribir_resultado("C06",resultado,dato)


#Analisis Usuarios por defecto
#--------------------------
archivo=carga.cargador("C02.txt")
arch_parseado=parser.parser_users(archivo)
resultado,dato=ana.analisis_c02(arch_parseado)
export.escribir_resultado("C02",resultado,dato)

#Analisis Log auditoria
#--------------------------
archivo=carga.cargador("C12.txt")
arch_parseado=parser.parser_auditlogs(archivo)
resultado,dato=ana.analisis_c12(arch_parseado)
export.escribir_resultado("C12",resultado,dato)


#Analisis contraseña
#--------------------------
archivo=carga.cargador("C08.html")
arch_parseado=parser.parser_passwords(archivo)
resultado,dato=ana.analisis_c08(arch_parseado)
export.escribir_resultado("C08",resultado,dato)



#Exportación de resultados a la matriz execel
export.guardar_salida()