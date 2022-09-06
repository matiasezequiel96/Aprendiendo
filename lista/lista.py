lista = ["string", 12, 12, 12.32, True, False]


#append --> es agregar un nuevo elemento al final de la lista // pasar un solo parametros
lista.append("hola")

#clear --> elimina todo los elementos de la lista, no necesita parametros
#lista.clear()

#copy --> copy la lista en un espacio de memoria diferente
lista2 = lista.copy()

# print(id(lista))
# print(id(lista2))

#count --> contar la cantidad de elementos pasados por parametro
contar = lista.count(12)

#extend --> añade un elementos nuevos al array existente
lista.extend([12, 23, 43, True])


#index --> retorna posicion del elemento en la lista
posicion = lista.index(12)
print(posicion)

#el primer parametro es el valor, segundo el comienzo del rango y el tercero el final del rango
a = lista.index(12, 5, 10)
print(a)

#insert --> agrega un nuevo elemento por indice
lista.insert(3, "superposicion")

#pop --> elemina por indice
lista.pop() # si no se pasa nada, elemina el ultimo
lista.pop(0)

#remove --> elemina el primer valor que encuentra en la lista
lista.remove(12)

#reverse --> retorna la lista de reversa
lista.reverse()


listaNum = [12, 43, 1, 54, 17, 52.32]
#sort --> ordena de menor a mayor // solo si son tipo int and float
listaNum.sort()
#print(listaNum)
#si se especifica que reverse sea True, ordena de mayor a menor
listaNum.sort(reverse=True)
#print(listaNum)
