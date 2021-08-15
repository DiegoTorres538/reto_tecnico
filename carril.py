import os

class carril():
    
    def __init__(self, vehiculo, jugador):
        self.vehiculo = vehiculo
        self.jugador = jugador
    
def movimiento(valor):
    pos = valor*100
    return pos


class podio():
    
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
        
def guardar(text):
    ruta = os.getcwd()+"/resultados.txt"
    with open(ruta,"a") as file:
        file.write(text)