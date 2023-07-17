import json

with open("ciclo_1/Codigos/archivos-json/lista.json", "r") as archivo:
    lista = json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

for elem in lista:
    print(elem, end=", ")