#Crear archivo json con una estructura de datos diccionarios

import json

"""midic = {1: "Lapiz",2:"Borrador",3:"Cuaderno",4:"Lapicero","valor":2500}
"""
midic2={
    "influencers":[
        {
            "name":"Jaxon",
            "edad":42,
            "work at":"Tech News"
        },
        {
            "name": "Miller",
            "edad":35,
            "work at":"IT Day"
        }
    ]
}

with open("archivos/JSON/diccionario.json", "w")as archivo:
    json.dump(midic2, archivo)
"""
with open("archivos/JSON/diccionario.json", "w")as archivo:
    json.dump(midic, archivo)
"""
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()