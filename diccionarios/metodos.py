# diccionario tiene clave (siempre tiene comillas simples o dobles)- valor
persona = {"nombre": "Ariel", "edad": 22, "estado_civil": False}


#persona.clear() #elimina todas las claves y valores



# OPERACIONES CRUD
# CREATE : crear
# READ : leer
# UPDATE : actualizar o cambiar 
# DELETE : borrar

#CREATE
persona = {"nombre": "Ariel", "edad": 22, "estado_civil": False}

#READ

# ----- Opcion N°1 ------
for x in persona:
    print(x, persona[x])
    

# ----- Opcion N°2 ------
for clave, valor in persona.items():
    print(clave, ":", valor)

print(persona["edad"]) # podes pasar una sola clave
print(persona.get("edad", "nombre")) #obtiene el valor de la clave, y se puede pasar mas de una clave pero no te muestra el valor

#UPDATE
persona.update({"gatos": True}) #si la clave no existe, la agrega
persona.update({"nombre": "Angel"}) # cambiar de valor 
persona["edad"] = 31 
print(persona)

#DELETE

#persona.clear() #elimina todas las claves y valores
del persona["estado_civil"] # borra una clave y valor especificada

persona1 = {"nombre": "Carlos"}
gato = persona.popitem() #popitem borra la ultima clave - valor del diccionario
print(persona)
persona1.update({gato})
print(persona1)