#DICCIONARIOS
"""alejandro = {"Nombre": "Alejandro", "Edad": 32, "Ciudad": "Barcelona", "aficiones": ["lectura","cine","videojuegos"]}
print(alejandro)

ana = {"Nombre": "Ana", "Edad": 42, "Ciudad": "Madrid","aficiones": ["pesca","natacion","escritura","cantar"]}
print(ana)

trabajadores = {0 : alejandro, 1:ana}
print(trabajadores)

print(f"La longuitud del diccionario de alejandro es: {len(alejandro)}")
print(f"La longuitud del diccionario los trabajador es: {len(trabajadores)}")

#UN DICCIONARIO NO PUEDE TENER CLAVES REPETIDAS
a ={ "año": 1996, "año": 2004}"""

#AÑADIR ELIMINAR Y MODIFICAR ELEMENTOS DICCIONARIO
alejandro = {"Nombre": "Alejandro", "Edad": 32, "Ciudad": "Barcelona", "aficiones": ["lectura","cine","videojuegos"]}
print(alejandro)

alejandro["Cargo"]= "CEO"
print(alejandro)

alejandro.update({"sueldo": 90000, "vacaciones": "muchas"})
print(alejandro)

print("Como eliminar elementos: ")
del alejandro["vacaciones"]
print(alejandro)
valor = alejandro.pop("cargo")
print(alejandro)
print(f"El valor eliminado es: {valor}")