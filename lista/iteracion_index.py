gatos = [["Raul", "Castaño con blanco"],
         ["Martin", "Castaño con negro", ["hola", ["Como estas"]]], 
         ["Poo", "Miel"], 
         ["Manchas", "Blanco con manchas"]]

cont1 = 0

for x in gatos:
    if len(x[0]) > 3:
        print("Nombre mayor a 3: ", x[0])
        cont1 += 1

print("Los cantidad de gatos mayores a 3:", cont1)
#for --> itera sobre una lista, tupla o diccionario
# x --> cada valor de la lista
#in --> cada valor de donde
#gatos --> la lista
for gato in gatos:
    print("este es de gatos:", gato)
    for cat in gato:
        print("este es de gato: ", cat)

#for se usar por lo general para iterar listas.

contador = 0
cantador2 = 0
#while es repetir una accion determinadas veces
while contador < 10:
    print("Hola", contador)
    if contador % 2 == 0:
        cantador2 += 1

    contador += 1 #contador = contador + 1

print("Contador = ", contador)
print("Contador2 = ", cantador2)

# indice1 = gatos[0][1]
# indice2 = gatos[1][2][1]
# print("Este es el indice: ", indice2)

# cont = 0

# while cont < len(gatos):
#     print(gatos[cont])
#     cont += 1 

# while True:
#     print("Si ingresa 0 se termina la ejecucion")
#     operacion = input("Ingrese un numero: ")
#     if operacion == "0":
#         break #termina la ejecucion del while
#     print(operacion)

# print("hola")

