

from ctypes.wintypes import HLOCAL


datos_personas = [["Manuel Juarez", 19823451, "Liverpool"], ["Silvana Paredes", 22709128, "Buenos Aires"], 
["Rosa Ortiz", 15123978, "Glasgow"], ["Luciana Hernandez", 38981374, "Lisboa"]] 

lugares = [["Buenos Aires","Argentina"], ["Glasgow","Escocia"], ["Lisboa", "Portugal"], ["Liverpool","Inglaterra"], ["Madrid","España"]]

while True:
    saludo = """
    Bienvenidos a Aeroparque
    """

    print(saludo)
    usuarios_nuevos = input("Ingrese su nombre, por favor: ")
    dni_usuarios = input ("Hola" + " " + usuarios_nuevos + ", " + "escriba su dni, por favor: ")
    destino_usuarios = input("Escriba su destino por favor: ")
    pais_destino = input("Escriba el pais, por favor: ")

    datos_personas.extend([[usuarios_nuevos + "," + " " + dni_usuarios + "," + " " + destino_usuarios]])
    lugares.extend([[destino_usuarios + ", " + pais_destino]])

    saludo_opciones = "Buenas tardes " + usuarios_nuevos + ":"
    texto_opciones = """
        [1] Ver el destino de su vuelo con su dni
        [2] Ver el pais al que viaja con su dni 
        [3] Salir
        """

    while True:
        print(saludo_opciones)
        print(texto_opciones)
        eleccion = input("Elija la opcion que desee: ") 
        if (eleccion == "1") or ( eleccion == "2"):   
            while True:
                if eleccion == "1":                
                    destino_dni = input("Coloque su dni para saber su destino: ")                
                    if destino_dni == dni_usuarios:                    
                        print(destino_usuarios)                    
                        pregunta_cant = input("¿Quiere ver la cantidad de pasajeros que van? [1]Si [2]No: ")
                        if pregunta_cant == "1":
                            pasajeros = 0
                            if destino_usuarios not in lugares:
                                pasajeros += 1
                                print("cant: ", pasajeros)
                                                                   
                        break                
                    else:                
                        print("Por favor ingrese su dni, Gracias.")            
                elif eleccion == "2":                
                    destino_dni_pais = input("Coloque su dni para saber el pais del destino: ")                
                    if destino_dni_pais == dni_usuarios:                
                        print(pais_destino)
                        break                                  
                    else:                
                        print("Por favor ingrese su dni, Gracias.")
        elif eleccion == "3":
            print("Hasta luego " + usuarios_nuevos)
            break