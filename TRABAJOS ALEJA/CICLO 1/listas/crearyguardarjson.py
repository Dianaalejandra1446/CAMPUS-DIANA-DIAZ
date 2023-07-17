import json
#PROGRAMA PRINCIPAl (debajo de las funciones de carga) IR AL PRINCIPIO
ruta = "CICLO 1\JSON\instituto.json"
dicdata = {}
"""cargarInfo(ruta,dicdata)"""

#CREAMOS FUNCION DE GUARDAR
def cargarInfo():
    fd = open(ruta, "r")
    #Verificar si tengo datos
    try:
        dic = json.load(fd)
    except Exception as e:
        dic = {}
    fd.close()
    print(dic)
    return dic
#GUARDAR INFO DICC PRINCIPAL
def cargar_estudiantes (infoestudiantes):
    with open(ruta, "w") as archivo:
        json.dump(infoestudiantes, archivo)

#EN CADA FUNCION 
#def agregar():
    infoestudiantes = cargarInfo()

#A lo ultimo de la funcion
    cargar_estudiantes(infoestudiantes)
