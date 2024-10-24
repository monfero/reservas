import datetime

def text2date(data_str):
    try:
        # Usamos strptime para convertir el string a un objeto datetime
        data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
        return data
    except ValueError:
        print("erro")

import json

class Reserva:

    def __init__(self, codigo, num_habitacion, data_ini, data_fin, prezo_habitacion):
        self.codigo = codigo
        self.num_habitacion = num_habitacion
        self.data_ini = data_ini
        self.data_fin = data_fin
        self.prezo_habitacion = prezo_habitacion

    def get_codigo(self):
        return self.codigo
 
    def set_codigo(self, value):
        self.codigo = value

    def get_num_habitacion(self):
        return self.num_habitacion

    def set_num_habitacion(self, value):
        self.num_habitacion = value

    def get_data_ini(self):
        return self.data_ini

    def set_data_ini(self, value):
        self.data_ini = value

    def get_data_fin(self):
        return self.data_fin

    def set_data_fin(self, value):
        self.data_fin = value

    def get_prezo_habitacion(self):
        return self.prezo_habitacion

    def set_prezo_habitacion(self, value):
        self.prezo_habitacion = value
    
    def print_reserva(self):
        print(f"Codigo: {self.codigo}, Habitación: {self.num_habitacion}")
        print(f"Entrada: {self.data_ini}, Saída: {self.data_fin}")
        print(f"Prezo habitación: {self.prezo_habitacion}")
        
    def export_to_json(self):
        """
        Exporta reserva a lista con obxecto JSON.
        """
        return [{
            "codigo": self.codigo,
            "num_habitacion": self.num_habitacion,
            "data_ini": self.data_ini,
            "data_fin": self.data_fin,
            "prezo_habitacion": self.prezo_habitacion
        }]

    def save_to_file(self, filename):
        """
        Garda reserva a disco

        Args:
            filename (str): Nome do ficheiro no que se gardará a reserva
        """
  
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                if data:
                    data.append(self.export_to_json()[0])
                else:
                    print("Non hai datos no ficheiro")
                    
        except FileNotFoundError:
                data = self.export_to_json()
            
            
        with open(filename, 'w') as f:
                json.dump(data,f)



class Reserva_Individual(Reserva):
    def __init__(self, codigo, num_habitacion, data_ini, data_fin, prezo_habitacion):
        super().__init__(codigo, num_habitacion, data_ini, data_fin, prezo_habitacion)

    def get_custo_reserva(self):
        dias = (text2date(self.data_fin) - text2date(self.data_ini)).days
        return dias*self.prezo_habitacion
    
    def print_reserva(self):
        super().print_reserva()
        print(f"Custo Reserva: {self.get_custo_reserva()}")
  


class Reserva_Grupal(Reserva):    
    def __init__(self, codigo, num_habitacion, data_ini, data_fin, prezo_habitacion, num_persoas):
        super().__init__(codigo, num_habitacion, data_ini, data_fin, prezo_habitacion)
        self.num_persoas = num_persoas

    def get_num_persoas(self):
        return self.num_persoas
    
    def set_num_persoas(self, value):
        self.num_persoas = value

    def get_custo_reserva(self):
        # Aplicar un descuento del 10% por persona adicional (máximo 50%) 
        dias = (text2date(self.data_fin) - text2date(self.data_ini)).days
        desconto = 1 - min(0.5, 0.1 * (self.num_persoas - 1))
        return dias*self.prezo_habitacion*desconto

    def print_reserva(self):
        super().print_reserva()
        print(f"Custo Reserva: {self.get_custo_reserva()}")

    def export_to_json(self):
        """
        Exporta reserva a lista con obxecto JSON.
        """
        return [{
            "codigo": self.codigo,
            "num_habitacion": self.num_habitacion,
            "data_ini": self.data_ini,
            "data_fin": self.data_fin,
            "prezo_habitacion": self.prezo_habitacion,
            "num_persoas": self.num_persoas
        }]