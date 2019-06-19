from Parser import *
import pandas as pd
from carga import *

class Analisis_idle ():
    
    def inactividad_correct(self,tiempo):
        return int(tiempo)<=15,int(tiempo)
    
    def analisis(self,nombre):
        car = Cargador()
        tiempo = car.cargar(nombre)
        return self.inactividad_correct(tiempo)

