from jugador import jugador, datos
from carro import lista_carros

def alias():
    jugador_list = []
    z = input("Ingrese su alias de jugador: ")
    jugador_list.append(jugador(z).nombre)
    return jugador_list
        
def elegir_conductor():
   aux = datos()
   players = []
   vald = True
   while vald:
        print("1)",aux[0].nombre)
        print("2)",aux[1].nombre)
        print("3)",aux[2].nombre)
        print("4)",aux[3].nombre)
        print("5)",aux[4].nombre)
        print("6)",aux[5].nombre)
        pilot = int(input("¿Cuál piloto desea?: "))
        if(pilot==1):
            players.append(aux[0].nombre)
            vald = None
        elif(pilot==2):
            players.append(aux[1].nombre)
            vald = None
        elif(pilot==3):
            players.append(aux[2].nombre)
            vald = None
        elif(pilot==4):
            players.append(aux[3].nombre)
            vald = None
        elif(pilot==5):
            players.append(aux[4].nombre)
            vald = None
        elif(pilot==6):
            players.append(aux[5].nombre)
            vald = None
        else:
            print("opción no válida, intente de nuevo")
   return players

def elegir_carro():
    aux_listcar = lista_carros()
    cars = []
    aux_vald = True
    while aux_vald:
        print("\n1)",aux_listcar[0].marca,aux_listcar[0].modelo)
        print("2)",aux_listcar[1].marca,aux_listcar[1].modelo)
        print("3)",aux_listcar[2].marca,aux_listcar[2].modelo)
        print("4)",aux_listcar[3].marca,aux_listcar[3].modelo)
        print("5)",aux_listcar[4].marca,aux_listcar[4].modelo)
        print("6)",aux_listcar[5].marca,aux_listcar[5].modelo)
        aux_cont = int(input("¿Qué Carro elige?: "))
        if(aux_cont==1):
            cars.append(str(aux_listcar[0].marca+" "+aux_listcar[0].modelo))
            aux_vald = None
        elif(aux_cont==2):
            cars.append(str(aux_listcar[1].marca+" "+aux_listcar[1].modelo))
            aux_vald = None
        elif(aux_cont==3):
            cars.append(str(aux_listcar[2].marca+" "+aux_listcar[2].modelo))
            aux_vald = None
        elif(aux_cont==4):
            cars.append(str(aux_listcar[3].marca+" "+aux_listcar[3].modelo))
            aux_vald = None
        elif(aux_cont==5):
            cars.append(str(aux_listcar[4].marca+" "+aux_listcar[4].modelo))
            aux_vald = None
        elif(aux_cont==6):
            cars.append(str(aux_listcar[5].marca+" "+aux_listcar[5].modelo))
            aux_vald = None
        else:
            print("opción no válida, intente de nuevo")
    return cars
    
    
    