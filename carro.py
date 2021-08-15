class carro():
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


def lista_carros():        
    carros_array = []
    carros_array.append(carro("Alfa Romeo", "Giulietta", "Verde"))
    carros_array.append(carro("Aston Martin", "DB9", "Amarillo"))
    carros_array.append(carro("Ferrari", "488 Spider", "Rojo"))
    carros_array.append(carro("Jaguar", "XF", "Negro"))
    carros_array.append(carro("Lamborghini", "Gallardo", "Azul"))
    carros_array.append(carro("Mercedes-Benz", "SLK", "Gris"))
    return carros_array
