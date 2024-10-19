from lib.funcionalidades import *

print("Benvido ao servizo de reservas")

opcion=0

while opcion!=6:
    print_menu()
    opcion=int(input('Escoller unha opción: '))
    match(opcion):
        case 1: 
            nova_reserva()
        case other: 
            print('Opción non dispoñible')