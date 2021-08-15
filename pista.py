class pista():
    
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud

def circuito1():      
    c1 = []
    c1.append(pista("Daytona",4200))
    c1.append(pista("Bristol",3600))
    c1.append(pista("IndianaPolis",5700)) #13500
    return c1

def circuito2():        
    c2 = []
    c2.append(pista("Charlotte",2900))
    c2.append(pista("Darlington",5200))
    c2.append(pista("Milwaukee",4600)) #12700
    return c2

def circuito3():        
    c3 = []
    c3.append(pista("Talladega",4300))
    c3.append(pista("Martinsville",5400))
    c3.append(pista("Richmond",3500)) #13200
    return c3

def eleccion_circuito():
    pista1 = circuito1()
    pista2 = circuito2()
    pista3 = circuito3()
    print("\n¿Cual circuito correrán?\n")
    print("1) Circuito 1, 3 Pistas con un total de 13500 m")
    print("2) Circuito 2, 3 Pistas con un total de 12700 m") 
    print("3) Circuito 3, 3 Pistas con un total de 13200 m")
    z = int(input("¿Que circuito eligen?: "))
    if(z==1):
        return pista1
    elif(z==2):
        return pista2
    else:
        return pista3