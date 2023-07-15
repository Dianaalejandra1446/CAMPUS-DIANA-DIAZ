#Leer un archivo json para recuperar la estructura de datos lista

import json

with open("archivos/JSON/diccionario.json","r") as archivo:
          midic = json.load(archivo)

if not archivo.closed:
        print("Cerrando archivo")
        archivo.close()

print("Diccionario:",midic)
print("\nDiccionario[influencers][1][name]:", midic["influencers"][1]["name"])