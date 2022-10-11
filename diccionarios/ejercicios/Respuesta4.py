"""4_ Escribir un programa que cree un diccionario vacío y lo vaya
 llenado con información sobre una persona 
 (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
 que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido 
 del diccionario.
"""

datos_personales = {}

preg_nombre = input("Ingrese su nombre: ")
datos_personales.update({"nombres": preg_nombre})
print(datos_personales)

preg_edad = int(input("Ingrese su edad: "))
datos_personales.update({"edad": preg_edad})
print(datos_personales)

preg_sexo = input("Ingrese su sexo: ")
datos_personales.update({"sexo": preg_sexo})
print(datos_personales)

preg_telefono = int(input("Ingrese su numero telefonico: "))
datos_personales.update({"telefono": preg_telefono})
print(datos_personales)

preg_correo = input("Ingrese su correo electronico: ")
datos_personales.update({"correo": preg_correo})
print(datos_personales)

preg_peso = input("Ingrese su peso: ")
datos_personales.update({"peso": preg_peso})
print(datos_personales)