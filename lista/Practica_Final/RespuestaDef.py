datos_personas = [["Manuel Juarez", 19823451, "Liverpool"], ["Silvana Paredes", 22709128, "Buenos Aires"], 
["Rosa Ortiz", 15123978, "Glasgow"], ["Luciana Hernandez", 38981374, "Lisboa"]] 

lugares = [["Buenos Aires","Argentina"], ["Glasgow","Escocia"], ["Lisboa", "Portugal"], ["Liverpool","Inglaterra"], ["Madrid","España"], ["Buenos Aires","Argentina"]]

def agregar_personas(lista):
    usuarios_nuevos = input("Ingrese su nombre, por favor: ")
    dni_usuarios = int(input("Hola" + " " + usuarios_nuevos + ", " + "escriba su dni, por favor: "))
    destino_usuarios = input("Escriba su destino por favor: ")
    lista.append([usuarios_nuevos, dni_usuarios, destino_usuarios])

def agregar_destino(lista2):
    destino_usuarios = input("Escriba su destino por favor: ")
    pais_destino = input("Escriba el pais, por favor: ")
    lista2.append([destino_usuarios, pais_destino])

def vuelo_dni():
    dni_usuarios = int(input("Hola escriba su dni, por favor: "))
    for x in datos_personas:
        if dni_usuarios == x[1]:
            print("El destino de su viaje es:", x[2])

def ciudad_cantidad():
    contador = 0
    destino_usuarios = input("Escriba su destino por favor: ")
    for x in lugares:
        if destino_usuarios == x[0]:
            contador += 1
    print("A ", destino_usuarios, "viajan", contador, "personas.")

def dni_pais():
    dni_usuarios = int(input("Hola escriba su dni, por favor: "))
    for x in datos_personas:
        if dni_usuarios == x[1]:
            for v in lugares:
                if x[2] == v[0]:
                    print("El pais de su viaje es:", v[1])

def pais_cantidad():
    contador = 0
    pais_destino = input("Escriba el pais, por favor: ")
    for x in lugares:
        if pais_destino == x[1]:
            contador += 1
    print("A ", pais_destino, "viajan", contador, "personas.")

def saludo():
    print("""
        Bienvenidos a Aeroparque
        [1] Desea agregar un pasajero
        [2] Desea agregar un destino
        [3] Ver el destino de su vuelo con su dni
        [4] Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad. 
        [5] Dado el DNI de un pasajero, ver a qué país viaja.
        [6] Dado un país, mostrar cuántos pasajeros viajan a ese país.
        [7] Salir
    """)

while True:
    saludo()
    
    eleccion = input("Elija la opcion que desee: ") 

    if eleccion == "1":
        agregar_personas(datos_personas)
    
    elif eleccion == "2":
        agregar_destino(lugares)

    elif eleccion == "3":
        vuelo_dni()

    elif eleccion == "4":
        ciudad_cantidad()

    elif eleccion == "5":
        dni_pais()
    
    elif eleccion == "6":
        pais_cantidad()

    elif eleccion == "7":
        print("Hasta luego!")
        break