from lib.funcionalidades import mostrar_detalle_reserva, print_menu, nova_reserva, mostrar_lista_reservas, load_reservas, cancelar_reserva, mostrar_custo_reserva, modificar_reserva

from lib.reserva import Reserva

print("Benvido ao servizo de reservas")

opcion=0
# load_reservas() carga a lista de reservas do ficheiro reservas.json e devolve unha lista coas instancias das clases Reserva
lista_reservas=load_reservas()

while opcion!=7:
    print_menu()
    while True:  # Iteramos ata que o usuario insira un enteiro válido
        try:
            opcion = int(input('Escoller unha opción: '))
            break
        except ValueError:
            print("Non é posible. Por favor, introduce un número.")
    
    match(opcion):
        case 1: 
            #reserva = Reserva()  # Instancia la clase Reserva
            reserva = nova_reserva()  # Pasa la instancia de Reserva a nova_reserva
            lista_reservas.append(reserva)
        case 2:
            cancelar_reserva(lista_reservas)
        case 3:
            mostrar_lista_reservas(lista_reservas)
        case 4:
            mostrar_detalle_reserva(lista_reservas)
        case 5:
            mostrar_custo_reserva(lista_reservas)
        case 6: 
            modificar_reserva(lista_reservas)
        case 7:
            print("Grazas por usar o servizo de reservas!")
        case other: 
            print('Opción non dispoñible')
