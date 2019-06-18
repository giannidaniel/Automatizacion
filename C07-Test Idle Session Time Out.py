from Parser import *
import pandas as pd
from carga import *

carga = carga()
ruta = (r'C:\Users\Dani\Desktop\Automatizacion\Entradas\C07.txt')
tiempo = carga.cargador(ruta)


def inactividad_correct(tiempo):
    return int(tiempo)<=15

print(inactividad_correct(tiempo[1]))



