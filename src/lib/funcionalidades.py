

def print_menu():
    print(f'(1) Nova reserva')
    print(f'(2) Borrar reserva')
    print(f'(3) Mostrar lista de reservas')
    print(f'(4) Mostrar Info de reserva')
    print(f'(5) Mostrar custo de reserva')
    print(f'(6) Saír')

def nova_reserva():
    print(f'Datos da reserva')
    codigo=input("Dame o codigo: ")
    num_habitacion=input("Número de habitación: ")
    data_ini=input('Data de entrada: ')
    data_fin=input('Data de saída: ')
    prezo_habitacion=int(input('Prezo da habitación: '))
    is_reserva_grupal=input('Trátase dunha reserva grupal?[s/n]: ')
    if is_reserva_grupal=='s':
        num_persoas=int(input('Dime o número de persoas da reserva: '))
    