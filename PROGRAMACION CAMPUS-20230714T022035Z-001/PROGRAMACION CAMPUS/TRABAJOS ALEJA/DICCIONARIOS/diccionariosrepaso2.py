persona = {"nombre": "Juan", "edad":33, "direccion": "Reforma 333"}

print (persona["nombre"])
print (persona.get("edad"))

for valor in persona.values():
    print(valor)

for llave in persona.keys():
    print(llave)

for elemento in persona.items():
    print(elemento)

for llave,valor in persona.items():
    print(llave, valor)

#ACTUALIZAR VALOR

persona["direccion"] = "Reforma 300"
print(persona)

#ACTUALIZAR VARIOS VALORES
persona.update({"direccion": "Reforma 200","altura": 1.70})
print(persona)

#AGREGAR LLAVE
persona["peso"] = 80
print(persona)

#BORRAR VALORES

persona.pop("peso")