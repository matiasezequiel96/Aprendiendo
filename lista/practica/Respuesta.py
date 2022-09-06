frutas = ["banana", "naranja", "frutilla"]
#Ejercicio 1
frutas.append("manzana")    # Agrega un solo elemento a la lista
frutas.append("sandia")
print(frutas)

#Ejercicio 2
posicion = frutas.index("naranja")  # Con esto se sabe donde esta ubicado el elemento elegido
print(posicion)

#Ejercicio 3
frutas.insert(4, "kiwi")  # agrega un elemento a la lista, con el hecho de elegir donde ponerlo
print(frutas)

#Ejercicio 5
frutas2 = frutas.copy()   # Copia la lista elegida, creando la misma lista pero con diferente id
frutas2.extend(["anana", "durazno", "uva"])     # Agrega varios elementos a la lista
print(frutas)
print(frutas2)

#Ejercicio 6
frutas2.clear()    # Limpia la lista, borra todo
print(frutas2)

frutas.pop(0)      # Elimina el elemento del indice indicado
frutas.pop(2)
frutas.pop(3)
print(frutas)

#Ejercicio 7
frutas.extend([12, 54, 541, 2]) # Agrega varios elementos a la lista
print(frutas)

#Ejercicio Numeros
numeros = [12, 32, 43, 54, 65]

#Ejercicio 1
numeros.reverse() # Lee la lista de derecha a izquierda
print(numeros)
print(len(numeros)) # len() devuelve el numero de elementos que hay en una lista