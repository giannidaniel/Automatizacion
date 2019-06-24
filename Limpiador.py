class Limpiador():
    #Esta Clase extrae la información generada por el script, eliminando las secciones de header, ffooter y errores
    def limpiar(self,archivo):
        return archivo.split(("-"*53)+"\n")[1]
