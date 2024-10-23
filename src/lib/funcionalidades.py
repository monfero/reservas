

def print_menu():
    print(f'(1) Nova reserva')
    print(f'(2) Borrar reserva')
    print(f'(3) Mostrar lista de reservas')
    print(f'(4) Mostrar Info de reserva')
    print(f'(5) Mostrar custo de reserva')
    print(f'(6) Saír')

def nova_reserva(reserva):
    print(f'Engadir reserva')
    
    # Get codigo
    while True:
        codigo = input("Dame o codigo: ")
        if len(codigo.strip()) > 0:
            break
        else:
            print("Error! Codigo debe ser al menos un caracter.")
            
    # Add codigo to Reserva object's datos dictionary
    reserva.add_dato('codigo', codigo)
    
    # Get num_habitacion
    while True:
        try:
            num_habitacion = int(input("Número de habitación: "))
            if num_habitacion > 0:
                break
            else:
                print("Error! Número da habitación debe ser maior que 0.")
        except ValueError:
            print("Error! Número da habitación debe ser un número enteiro.")

    # Add num_habitacion to Reserva object's datos dictionary
    reserva.add_dato('num_habitacion', num_habitacion)
    
    # Get data_ini and data_fin
    while True:
        try:
            from datetime import datetime
            data_ini = input('Data de entrada (dd/mm/aaaa): ')
            data_fin = input('Data de saída (dd/mm/aaaa): ')

            if len(data_ini.strip()) > 0 and len(data_fin.strip()) > 0:
                # Validate date format
                datetime.strptime(data_ini, '%d/%m/%Y')
                datetime.strptime(data_fin, '%d/%m/%Y')

                if data_ini <= data_fin:
                    break
                else:
                    print("Error! A data de entrada debe ser anterior ou igual a data de saída.")
            else:
                print("Error! Ambas datas deben ter algún caracter.")
        except ValueError:
            print("Error! As datas deben estar no formato dd/mm/aa.")

    # Add data_ini and data_fin to Reserva object's datos dictionary
    reserva.add_dato('data_ini', data_ini)
    reserva.add_dato('data_fin', data_fin)
    
    # Get prezo_habitacion
    while True:
        try:
            prezo_habitacion = int(input('Prezo da habitación: '))
            if prezo_habitacion > 0:
                break
            else:
                print("Error! O prezo debe ser maior que 0.")
        except ValueError:
            print("Error! O prezo debe ser um número enteiro.")

    # Add prezo_habitacion to Reserva object's datos dictionary
    reserva.add_dato('prezo_habitacion', prezo_habitacion)
    
    # Get is_reserva_grupal and num_persoas
    while True:
        is_reserva_grupal = input('Trátase dunha reserva grupal?[s/n]: ')
        if is_reserva_grupal.lower() == 's':
            break
        elif is_reserva_grupal.lower() == 'n':
            print("Reserva grupal cancelada.")
            return
        else:
            print("Error! O valor debe ser 's' ou 'n'.")

    num_persoas = input('Dime o número de persoas da reserva: ')
    while not num_persoas.isdigit():
        print("Error! Por favor, introduce un número entero.")
        num_persoas = input('Dime o número de persoas da reserva: ')

    # Add is_reserva_grupal and num_persoas to Reserva object's datos dictionary
    reserva.add_dato('is_reserva_grupal', is_reserva_grupal)
    reserva.add_dato('num_persoas', num_persoas)

    print('Reserva finalizada')
    
def mostrar_lista_reservas(reservas):
    print("\nLista de Reservas:\n")
    for reserva in reservas:
        reserva.print_values()
        print("\n")
    print("\n")

    