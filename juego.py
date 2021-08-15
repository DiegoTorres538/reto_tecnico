from carril import carril, movimiento, guardar, podio
from inicio import alias, elegir_conductor, elegir_carro
from pista import eleccion_circuito
from random import randint
import time

oro = "Primer lugar\n"
plata = "Segundo lugar\n"
bronce = "Tercer lugar\n"
print("Saludos Jugadores elijan sus Alias")
print("\nJugador #1")
alias1 = alias()
print("\n¿Qué piloto elige?\n")
player1 = elegir_conductor()
car1 = elegir_carro()
print("\nJugador #2")
alias2 = alias()
print("\n¿Qué piloto elige?\n")
player2 = elegir_conductor()
car2 = elegir_carro()
print("\nJugador #3")
alias3 = alias()
print("\n¿Qué piloto elige?\n")
player3 = elegir_conductor()
car3 = elegir_carro()
datas = "Datos de los competidores:\n"
guardar(datas)
d1 = "\nEl jugador "+str(alias1[0])+" conduce un "+str(car1[0])+" tiene como piloto a "+str(player1[0])
guardar(d1)
d2 = "\nEl jugador "+str(alias2[0])+" conduce un "+str(car2[0])+" tiene como piloto a "+str(player2[0])
guardar(d2)
d3 = "\nEl jugador"+str(alias3[0])+" conduce un "+str(car3[0])+" tiene como piloto a"+str(player3[0]+"\n")
guardar(d3)
circuitos = eleccion_circuito()
carril1 = carril(car1[0],alias1[0])
carril2 = carril(car2[0],alias2[0])
carril3 = carril(car3[0],alias3[0])
for i in range(3):
    print("\nLa Carrera #",i+1, "será en la pista",circuitos[i].nombre,"con una distancia de",circuitos[i].longitud,"metros")
    print("\nEl carril 1 lo ocupará",carril1.jugador,"usando el coche",carril1.vehiculo)
    print("\nEl carril 2 lo ocupará",carril2.jugador,"usando el coche",carril2.vehiculo)
    print("\nEl carril 3 lo ocupará",carril3.jugador,"usando el coche",carril3.vehiculo)
    print("\nLa carrera comenzará en\n")
    for r in reversed(range(5)):
        print(r+1)
        time.sleep(1)
    print("\nComiencen!!!")
    aux_cont = 1
    pos1 = 0
    pos2 = 0
    pos3 = 0
    competidores = True
    while competidores:
        if(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos1>pos2 and pos2>pos3):
            podio1 = podio(carril1.jugador,oro)
            podio2 = podio(carril2.jugador,plata)
            podio3 = podio(carril3.jugador,bronce)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos1>pos2 and pos3>pos2):
            podio1 = podio(carril1.jugador,oro)
            podio2 = podio(carril2.jugador,bronce)
            podio3 = podio(carril3.jugador,plata)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos2>pos1 and pos1>pos3):
            podio1 = podio(carril1.jugador,plata)
            podio2 = podio(carril2.jugador,oro)
            podio3 = podio(carril3.jugador,bronce)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos2>pos1 and pos3>pos2):
            podio1 = podio(carril1.jugador,bronce)
            podio2 = podio(carril2.jugador,oro)
            podio3 = podio(carril3.jugador,plata)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos3>pos1 and pos1>pos2):
            podio1 = podio(carril1.jugador,plata)
            podio2 = podio(carril2.jugador,bronce)
            podio3 = podio(carril3.jugador,oro)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos3>pos2 and pos2>pos1):
            podio1 = podio(carril1.jugador,bronce)
            podio2 = podio(carril2.jugador,plata)
            podio3 = podio(carril3.jugador,oro)
            x = "\nEn la pista " +str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(y)
            z= str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(z)
            zz = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(zz)
            competidores = None
        elif(pos1>=circuitos[i].longitud and pos2<circuitos[i].longitud and pos3<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril1.jugador,"ha finalizado")
            aux_val2 = randint(1,6)
            auxr2 = movimiento(aux_val2)
            time.sleep(0.5)
            pos2 = pos2 + auxr2
            print(carril2.jugador,"avanzó",auxr2,"metros\n")
            aux_val3 = randint(1,6)
            auxr3 = movimiento(aux_val3)
            time.sleep(0.5)
            pos3 = pos3 + auxr3
            print(carril3.jugador,"avanzó",auxr3,"metros\n")
            aux_cont = aux_cont+1
        elif(pos2>=circuitos[i].longitud and pos1<circuitos[i].longitud and pos3<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril2.jugador,"ha finalizado")
            aux_val = randint(1,6)
            auxr = movimiento(aux_val)
            pos1 = pos1 + auxr
            time.sleep(0.5)
            print(carril1.jugador,"avanzó",auxr,"metros\n")
            aux_val3 = randint(1,6)
            auxr3 = movimiento(aux_val3)
            time.sleep(0.5)
            pos3 = pos3 + auxr3
            print(carril3.jugador,"avanzó",auxr3,"metros\n")
            aux_cont = aux_cont+1
        elif(pos3>=circuitos[i].longitud and pos1<circuitos[i].longitud and pos2<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril3.jugador,"ha finalizado")
            aux_val = randint(1,6)
            auxr = movimiento(aux_val)
            pos1 = pos1 + auxr
            time.sleep(0.5)
            print(carril1.jugador,"avanzó",auxr,"metros\n")
            aux_val2 = randint(1,6)
            auxr2 = movimiento(aux_val2)
            time.sleep(0.5)
            pos2 = pos2 + auxr2
            print(carril2.jugador,"avanzó",auxr2,"metros\n")
            aux_cont = aux_cont+1
        elif(pos1>=circuitos[i].longitud and pos2>=circuitos[i].longitud and pos3<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril1.jugador,"ha finalizado")
            print(carril2.jugador,"ha finalizado")     
            aux_val3 = randint(1,6)
            auxr3 = movimiento(aux_val3)
            time.sleep(0.5)
            pos3 = pos3 + auxr3
            print(carril3.jugador,"avanzó",auxr3,"metros\n")
            aux_cont = aux_cont+1
        elif(pos2>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos1<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril2.jugador,"ha finalizado")
            print(carril3.jugador,"ha finalizado")     
            aux_val = randint(1,6)
            auxr = movimiento(aux_val)
            time.sleep(0.5)
            pos1 = pos1 + auxr
            print(carril1.jugador,"avanzó",auxr,"metros\n")
            aux_cont = aux_cont+1
        elif(pos1>=circuitos[i].longitud and pos3>=circuitos[i].longitud and pos2<circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril1.jugador,"ha finalizado")
            print(carril3.jugador,"ha finalizado")     
            aux_val2 = randint(1,6)
            auxr2 = movimiento(aux_val2)
            time.sleep(0.5)
            pos2 = pos2 + auxr2
            print(carril2.jugador,"avanzó",auxr2,"metros\n")
            aux_cont = aux_cont+1
        elif(pos1>=circuitos[i].longitud and pos2==circuitos[i].longitud and pos3==circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril1.jugador,"ha finalizado")
            print("Los jugadores",carril2.jugador,carril3.jugador,"empataron")
            podio1 = podio(carril1.jugador,oro)
            podio2 = podio(carril2.jugador,plata)
            podio3 = podio(carril3.jugador,plata)
            x = "\nEn la pista "+str(circuitos[i].nombre)+"\n"
            guardar(x)
            yy = str(podio1.nombre)+" obtuvo el "+str(podio1.posicion)
            guardar(yy)
            y = "los jugadores "+str(podio2.nombre)+","+str(podio3.nombre)+" empataron el "+str(podio2.posicion)
            guardar(y)
            competidores = None
        elif(pos2>=circuitos[i].longitud and pos1==circuitos[i].longitud and pos3==circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril2.jugador,"ha finalizado")
            print("Los jugadores",carril1.jugador,carril3.jugador,"empataron")
            podio1 = podio(carril1.jugador,plata)
            podio2 = podio(carril2.jugador,oro)
            podio3 = podio(carril3.jugador,plata)
            x = "\nEn la pista "+str(circuitos[i].nombre)+"\n"
            guardar(x)
            yy = str(podio2.nombre)+" obtuvo el "+str(podio2.posicion)
            guardar(yy)
            y = "los jugadores "+str(podio1.nombre)+","+str(podio3.nombre)+" empataron el "+str(podio1.posicion)
            guardar(y)
            competidores = None
        elif(pos3>=circuitos[i].longitud and pos1==circuitos[i].longitud and pos2==circuitos[i].longitud):
            print("\nRonda",aux_cont,"\n")
            print(carril3.jugador,"ha finalizado")
            print("Los jugadores",carril1.jugador,carril2.jugador,"empataron")
            podio1 = podio(carril1.jugador,plata)
            podio2 = podio(carril2.jugador,plata)
            podio3 = podio(carril3.jugador,oro)
            x = "\nEn la pista "+str(circuitos[i].nombre)+"\n"
            guardar(x)
            yy = str(podio3.nombre)+" obtuvo el "+str(podio3.posicion)
            guardar(yy)
            y = "los jugadores "+str(podio1.nombre)+","+str(podio2.nombre)+" empataron el "+str(podio1.posicion)
            guardar(y)
            competidores = None
        elif(pos1==circuitos[i].longitud and pos2==circuitos[i].longitud and pos3==circuitos[i].longitud):
            print("Los jugadores",carril1.jugador,carril2.jugador,carril3.jugador,"empataron")
            podio1 = podio(carril1.jugador,oro)
            podio2 = podio(carril2.jugador,oro)
            podio3 = podio(carril3.jugador,oro)
            x = "\nEn la pista "+str(circuitos[i].nombre)+"\n"
            guardar(x)
            y = "los jugadores "+str(podio1.nombre)+","+str(podio2.nombre)+","+str(podio3.nombre)+" empataron el "+str(podio1.posicion)
            guardar(y)
            competidores = None
        else:
            print("\nRonda",aux_cont,"\n")
            val1 = randint(1,6)
            aux1 = movimiento(val1)
            pos1 = pos1 + aux1
            val2 = randint(1,6)
            aux2 = movimiento(val2)
            pos2 = pos2 + aux2
            val3 = randint(1,6)
            aux3 = movimiento(val3)
            pos3 = pos3 + aux3
            print(carril1.jugador,"avanzó",aux1,"metros\n")
            time.sleep(0.5)
            print(carril2.jugador,"avanzó",aux2,"metros\n")
            time.sleep(0.5)
            print(carril3.jugador,"avanzó",aux3,"metros\n")
            aux_cont = aux_cont+1

print("#############La Carrera Finalizó###############")
print("Revisa el archivo resultados.txt en la carpeta para revisar los resultados de las carreras del circuito elegido")
