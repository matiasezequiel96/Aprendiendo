# moneda = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
# print()
# while True:
#     eleccion = input("Escriba su divisa deseada: ")
#     print("Esta es su moneda: ", moneda[eleccion])
#     if eleccion == "Salir":
#         break

#The try block will generate a NameError, because x is not defined:
moneda = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
try:
  eleccion = input("Escriba su divisa deseada: ")
  print("Esta es su moneda: ", moneda[eleccion])

except KeyError:
  print("Esa moneda no existe")