from lib.funcionalidades import print_menu, nova_reserva, mostrar_lista_reservas


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
    


print("Benvido ao servizo de reservas")

opcion=0
lista_reservas=[]

while opcion!=6:
    print_menu()
    while True:  # Iteramos ata que o usuario insira un enteiro válido
        try:
            opcion = int(input('Escoller unha opción: '))
            break
        except ValueError:
            print("Non é posible. Por favor, introduce un número.")
    
    match(opcion):
        case 1: 
            reserva = Reserva()  # Instancia la clase Reserva
            nova_reserva(reserva)  # Pasa la instancia de Reserva a nova_reserva
            lista_reservas.append(reserva)
        case 3:
            mostrar_lista_reservas(lista_reservas)
        case other: 
            print('Opción non dispoñible')
