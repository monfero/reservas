
class Reserva:
    def __init__(self):
        self.datos = {}

    def add_dato(self, nombre, valor):
        self.datos[nombre] = valor

    def get_datos(self):
        return self.datos
    
    def print_values(self):
        for key, value in self.datos.items():
            print(f"{key}: {value}")

class Reserva_Individual(Reserva):
    def __init__(self, id_reserva=None):
        super().__init__()
        self.id_reserva = id_reserva

    
class Reserva_Grupal(Reserva):
    def __init__(self, id_grupo=None):
        super().__init__()
        self.id_grupo = id_grupo
