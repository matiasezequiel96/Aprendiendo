datos_personas = [["Manuel Juarez", 19823451, "Liverpool"], ["Silvana Paredes", 22709128, "Buenos Aires"], 
["Rosa Ortiz", 15123978, "Glasgow"], ["Luciana Hernandez", 38981374, "Lisboa"]] 

lugares = [["Buenos Aires","Argentina"], ["Glasgow","Escocia"], ["Lisboa", "Portugal"], ["Liverpool","Inglaterra"], ["Madrid","España"], ["Buenos Aires","Argentina"]]

def agregar_personas(lista):
    usuarios_nuevos = input("Ingrese su nombre, por favor: ")
    dni_usuarios = int(input("Hola" + " " + usuarios_nuevos + ", " + "escriba su dni, por favor: "))
    destino_usuarios = input("Escriba su destino por favor: ")
    lista.append([usuarios_nuevos, dni_usuarios, destino_usuarios])

while True:
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
    
    eleccion = input("Elija la opcion que desee: ") 
    if eleccion == "1":
        agregar_personas(datos_personas)
    
    elif eleccion == "2":
        destino_usuarios = input("Escriba su destino por favor: ")
        pais_destino = input("Escriba el pais, por favor: ")
        lugares.append([destino_usuarios, pais_destino])
    
    elif eleccion == "3":
        dni_usuarios = int(input("Hola escriba su dni, por favor: "))
        for x in datos_personas:
            if dni_usuarios == x[1]:
                print("El destino de su viaje es:", x[2])

    elif eleccion == "5":
        dni_usuarios = int(input("Hola escriba su dni, por favor: "))
        for x in datos_personas:
            if dni_usuarios == x[1]:
                for v in lugares:
                    if x[2] == v[0]:
                        print("El pais de su viaje es:", v[1])
    
    elif eleccion == "6":
            contador = 0
            pais_destino = input("Escriba el pais, por favor: ")
            for x in lugares:
                if pais_destino == x[1]:
                    contador += 1
            print("A,", pais_destino, "viajan", contador, "personas.")

    elif eleccion == "7":
        print("Hasta luego!")
        break
    # saludo_opciones = "Buenas tardes " + usuarios_nuevos + ":"


    # while True:
    #     print(saludo_opciones)
    #     print(texto_opciones)
    #     eleccion = input("Elija la opcion que desee: ") 
    #     if (eleccion == "1") or ( eleccion == "2"):   
    #         while True:
    #             if eleccion == "1":                
    #                 destino_dni = input("Coloque su dni para saber su destino: ")                
    #                 if destino_dni == dni_usuarios:                    
    #                     print(destino_usuarios)                    
    #                     pregunta_cant = input("¿Quiere ver la cantidad de pasajeros que van? [1]Si [2]No: ")
    #                     if pregunta_cant == "1":
    #                         pasajeros = 0
    #                         if destino_usuarios not in lugares:
    #                             pasajeros += 1
    #                             print("cant: ", pasajeros)
                                                                   
    #                     break                
    #                 else:                
    #                     print("Por favor ingrese su dni, Gracias.")            
    #             elif eleccion == "2":                
    #                 destino_dni_pais = input("Coloque su dni para saber el pais del destino: ")                
    #                 if destino_dni_pais == dni_usuarios:                
    #                     print(pais_destino)
    #                     break                                  
    #                 else:                
    #                     print("Por favor ingrese su dni, Gracias.")
    #     elif eleccion == "3":
    #         print("Hasta luego " + usuarios_nuevos)
    #         break
