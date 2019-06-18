from Parser import *
import pandas as pd

carga = Parser()
archivo = (r'C:\Users\Dani\Desktop\Automatizacion\entradas\salida.txt')
dataframe = carga.parser_discos(archivo)
data=dataframe[["FileSystem"]]
#Filtra los valores == 'NTFS' de la columna FileSystem y devuelve false si hay almenos 1 valor distinto de 'NTFS'
if data[data['FileSystem']!='NTFS'].empty:
    print('OK')
else:
    print('NO OK')

# for i in range(len(data['FileSystem'])) :
#     if data['FileSystem'][i] == 'NTFS':
#         print('OK')
#     else:
#         print('NO OK')
    
    