frutas = {"naranja": 100, "manzana": 120, "banana": 115, "frutilla": 150}

preg_cliente = input("Que fruta desea?: ")
preg_cliente2 = int(input("Cuantos kilos va a llevar?: "))

def precio_total(x):
    precio = preg_cliente2 * frutas[x]
    print("Sale: ", precio)
                
if preg_cliente2 > 0:

    if preg_cliente == "naranja":
        precio_total("naranja")
                
    elif preg_cliente == "manzana":
        precio_total("manzana")
                
    elif preg_cliente == "banana":
        precio_total("banana")

    elif preg_cliente == "frutilla":
        precio_total("frutilla")
    else:
        print("Su fruta no esta en la tabla, ingrese otra.")