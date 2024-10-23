from lib.funcionalidades import print_menu, nova_reserva


print("Benvido ao servizo de reservas")

opcion=0

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
            nova_reserva()
        case other: 
            print('Opción non dispoñible')
