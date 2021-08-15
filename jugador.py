class jugador():
    
    def __init__(self, nombre):
        self.nombre = nombre
        #self.edad = int(input("Edad:"))
        

class conductor():
    
    def __init__(self, nombre, nacionalidad, edad, sexo):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad = edad
        self.sexo = sexo

def datos():
    drivers = []
    drivers.append(conductor("Danica Patrick","Estados Unidos", "39", "Femenino"))
    drivers.append(conductor("Reed Sorenson","Alemania", "35", "Masculino"))
    drivers.append(conductor("Daniel Suarez","México", "30", "Masculino"))
    drivers.append(conductor("Erika Jones","Estados Unidos", "33", "Femenino"))
    drivers.append(conductor("J.J Yeley","Francia", "44", "Masculino"))
    drivers.append(conductor("Dimitri Keselowski","Rusia", "42", "Masculino"))
    return drivers