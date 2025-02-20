from vehiculo import Vehiculo

class NodeVehiculo:
    def __init__(self, data: Vehiculo):
        self.data = data
        self.next = None
        self.prev = None
