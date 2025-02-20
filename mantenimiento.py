import datetime

class Mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nueva_fecha):
        try:
            datetime.datetime.strptime(nueva_fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe tener el formato dd/mm/yyyy.")
        self.__fecha = nueva_fecha

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @property
    def costo(self):
        return self.__costo
    
    @costo.setter
    def costo(self, nuevo_costo):
        try:
            nuevo_costo = float(nuevo_costo)
        except:
            raise ValueError("El costo debe ser un número.")
        if nuevo_costo <= 0:
            raise ValueError("El costo debe ser un número positivo.")
        self.__costo = nuevo_costo


        
