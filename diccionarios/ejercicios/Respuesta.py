moneda = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}

for x in moneda.items():
    eleccion = input("Escriba su divisa deseada: ")
    if eleccion == x:
        print("Esta es su moneda: ", y)
    else:
        print("No esta")