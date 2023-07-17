#Crear archivo json con una estructura de datos lista

import json

lista = [10,20,30,40,60]

with open("archivos/JSON/lista.json", "w")as archivo:
    json.dump(lista, archivo)
    print("Se ha escrito en disco")

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Se ha cerrado el archivo")