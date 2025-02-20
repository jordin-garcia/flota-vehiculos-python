from node_mantenimiento import NodeMantenimiento
from mantenimiento import Mantenimiento
from tabulate import tabulate
import datetime
import re

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.historial_mantenimiento = None

    @property
    def placa(self):
        return self.__placa
        
    @placa.setter
    def placa(self, nueva_placa):
        if not re.fullmatch(r'\d{7}', nueva_placa):
            raise ValueError("(*) La placa debe tener 7 caracteres alfanuméricos.")
        self.__placa = nueva_placa
                   
    @property
    def marca(self):
        return self.__marca
        
    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    @property
    def modelo(self):
        return self.__modelo
        
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    @property
    def año(self):
         return self.__año
        
    @año.setter
    def año(self, nuevo_año):
        try:
            nuevo_año = int(nuevo_año)
        except:
            raise ValueError("El año debe ser un número entero.")
        current_year = datetime.datetime.now().year
        if nuevo_año < 1900 or nuevo_año > current_year:
            raise ValueError(f"El año debe ser entre 1900 y {current_year}.")
        self.__año = nuevo_año

    @property
    def kilometraje(self):
         return self.__kilometraje
        
    @kilometraje.setter
    def kilometraje(self, nuevo_kilometraje):
        try:
            nuevo_kilometraje = float(nuevo_kilometraje)
        except:
            raise ValueError("El kilometraje debe ser un número.")
        if nuevo_kilometraje < 0:
            raise ValueError("El kilometraje debe ser un número positivo.")
        self.__kilometraje = nuevo_kilometraje
    
    #Lista Enlazada de Mantenimientos
    
    def is_empty(self):
        return self.historial_mantenimiento is None
    
    def agregar_mantenimiento(self, mantenimiento: Mantenimiento):
        new_node = NodeMantenimiento(mantenimiento)
        if self.historial_mantenimiento is None:
            self.historial_mantenimiento = new_node
        else:
            current = self.historial_mantenimiento
            while current.next is not None:
                current = current.next
            current.next = new_node

    def calcular_costo_total_mantenimiento(self):
        total = 0
        current = self.historial_mantenimiento
        while current is not None:
            total += int(current.data.costo)
            current = current.next
        return total 

    def consultar_historial_mantenimiento(self):
        headers = ["Fecha", "Descripcion", "Costo"]
        rows = []
        current = self.historial_mantenimiento
        while current:
            mantenimiento = current.data
            rows.append([mantenimiento.fecha, mantenimiento.descripcion, mantenimiento.costo])
            current = current.next
        total = self.calcular_costo_total_mantenimiento()
        # Agrega una fila extra para mostrar el total debajo de la columna "Costo"
        rows.append(["", "Costo Total:", total])
        print(tabulate(rows, headers, tablefmt="grid"))

       
    
        
