from node_vehiculo import NodeVehiculo
from vehiculo import Vehiculo
from tabulate import tabulate

class FlotaVehiculos:

    #Lista Doblemente Enlazada

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data: Vehiculo):
        new_node = NodeVehiculo(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, target):
        current = self.head
        while current:
            if current.data.placa == target:
                return current.data
            current = current.next
        return None

    def remove(self, target):
        current = self.head
        while current:
            if current.data.placa == target:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
            current = current.next
  
    def print_list(self):
        headers = ["Placa", "Marca", "Modelo", "Año", "Kilometraje"]
        rows = []
        current = self.head
        while current:
            vehiculo = current.data
            rows.append([vehiculo.placa, vehiculo.marca, vehiculo.modelo, vehiculo.año, vehiculo.kilometraje])
            current = current.next
        print(tabulate(rows, headers, tablefmt="grid"))


