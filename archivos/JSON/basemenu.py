""""import json

def cargarInfo(ruta,dic):
    fd = open(ruta, "a+")
    fd.seek(0)
    #Verificar si tengo datos
    try:
        dic = json.load(fd)
    except Exception as e:
        print(e)
        dic = {}
    fd.close()
    print(dic)

#PROGRAMA PRINCIPAl (debajo de las funciones de carga)
ruta ="archivos/JSON/instituto.json"
dicdata = {}
cargarInfo(ruta,dicdata)

def menu(ruta):
    pass
def estudiantes(ruta):
    pass
def reportes(ruta):
    pass

while True:
    op = menu()
    if op == "1":
        estudiantes(ruta)
    elif op == "2":
        notas(ruta)
    elif op == "3":
        reportes(ruta)
    elif op == "4":
        print("Gracias por usar este programa")
        input("Presione cualquier tecla para salir...")
        break""""