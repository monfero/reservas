from lib.reserva import *

def print_menu():
    print(f'(1) Nova reserva')
    print(f'(2) Borrar reserva')
    print(f'(3) Mostrar lista de reservas')
    print(f'(4) Mostrar Info de reserva')
    print(f'(5) Mostrar custo de reserva')
    print(f'(6) Saír')


def pedir_codigo():
    # Get codigo
    while True:
        codigo = input("Dame o codigo: ")
        if len(codigo.strip()) > 0:
            break
        else:
            print("Error! Codigo debe ser al menos un caracter.")
        return codigo

def pedir_num_habitacion():
    # Get numero de habitacion
    while True:
        try:
            num_habitacion = int(input("Número de habitación: "))
            if num_habitacion > 0:
                break
            else:
                print("Error! Número da habitación debe ser maior que 0.")
        except ValueError:
            print("Error! Número da habitación debe ser un número enteiro.")
    return num_habitacion

def pedir_datas():
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
            print("Error! As datas deben estar no formato dd/mm/aaaaa.")
    return [data_ini,data_fin]

def pedir_prezo_habitacion():
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
    return prezo_habitacion
 


def nova_reserva():
    print(f'Engadir reserva')
    
    codigo = pedir_codigo()           
    num_habitacion = pedir_num_habitacion()
    datas = pedir_datas()
    data_ini = datas[0]
    data_fin = datas[1]
    prezo_habitacion = pedir_prezo_habitacion()


    # Get is_reserva_grupal and num_persoas
    while True:
        is_reserva_grupal = input('Trátase dunha reserva grupal?[s/n]: ')
        if is_reserva_grupal.lower() == 's':
            num_persoas = input('Dime o número de persoas da reserva: ')
            while not num_persoas.isdigit():
                print("Error! Por favor, introduce un número entero.")
                num_persoas = input('Dime o número de persoas da reserva: ')
            print("Reserva grupal: 10% de desconto por persoa ata un máximo de 50%")
            reserva = Reserva_Grupal(codigo, num_habitacion, data_ini, data_fin, prezo_habitacion, int(num_persoas))
            break
        elif is_reserva_grupal.lower() == 'n':
            print("Reserva individual")
            reserva = Reserva_Individual(codigo, num_habitacion, data_ini, data_fin, prezo_habitacion)
            break
        else:
            print("Error! O valor debe ser 's' ou 'n'.")

    print('Reserva finalizada\n')
    
    reserva.print_reserva()
    reserva.save_to_file('reservas.json')
    print("\n")
    
    return reserva
    
def mostrar_lista_reservas(reservas):
    print(20*"#")
    print("Lista de Reservas:")
    print(20*"#")
    for reserva in reservas:
        reserva.print_reserva()
        print("\n")
    print(20*"#")

def load_reservas():
    try:
        with open('reservas.json', 'r') as file:
            data = json.load(file)
            reservas = []
            for reserva in data:
                if 'num_persoas' in reserva:
                    r = Reserva_Grupal(reserva['codigo'], reserva['num_habitacion'], reserva['data_ini'], reserva['data_fin'], reserva['prezo_habitacion'], reserva['num_persoas'])
                else:
                    r = Reserva_Individual(reserva['codigo'], reserva['num_habitacion'], reserva['data_ini'], reserva['data_fin'], reserva['prezo_habitacion'])
                reservas.append(r)
            return reservas
    except FileNotFoundError:
        print("Non hai reservas gardadas.")
        return []
    