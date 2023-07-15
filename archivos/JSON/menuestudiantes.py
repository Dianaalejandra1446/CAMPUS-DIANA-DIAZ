import json

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
    print("1.1 Agregar")
    print("1.2 Modificar")
    print("1.3 Eliminar")
    print("1.4 Buscar")
    print("1.5 Salir")
    while True:
        elegir = estudiantes()
        if elegir == 1.1:
            agregar()
        elif elegir == 1.2:
            modificar()
        elif elegir == 1.3:
            eliminar()
        elif elegir == 1.4:
            buscar()
        elif elegir == 1.5:
            print("Haz salido de menu estudiantes")
            break
    def agregar():

        infoestudiantes = {}
        id = int(input("Ingrese id del estudiante: "))
        infoestudiantes[id] = {}
        print(f"El id del estudiante es {id}")

        nombreEstu = input("Ingrese el nombre del estudiante: ")
        infoestudiantes[id]["Nombre estudiante"] = nombreEstu
        print(f"El nombre del estudiante es {nombreEstu}")

        sexo = input("Ingrese el sexo del estudiante F o M")
        infoestudiantes[id]["Sexo estudiante"] = sexo
        print(f"El sexo del estudiante es {sexo}")

        grado = input("Ingrese el grado del estudiante")
        infoestudiantes[id]["Grado estudiante"] = grado

        agregarotro = input("Desea agregar otro estudiante? si/no")
        if agregarotro == "si":
            return agregar

        input("---> Presione ENTER para continuar")



    def modificar():
        print("Modificar empleado: ")
        print("----Seleccione el numero de lo que quiere modificar---- ")
        print("\n 1.Modificar nombre \n 2.Modificar sexo \n 3.Modicar grado")

        while True:
            infoestudiantes = {}
            buscarid = input("Ingrese el id del empleado que desea modificar: ")
            if buscarid in infoestudiantes:
                print("ID ENCONTRADO")
                modificar = int(input("Ingrese un numero: "))
                if modificar == 1:
                    nuevonombre= input("Ingrese el nuevo nombre: ")
                    infoestudiantes[buscarid]["Nombre estudiante"] = nuevonombre
                    break
                elif modificar == 2:
                    actualizarsexo = input("Ingrese nuevo sexo del estudiante: ")
                    infoestudiantes[buscarid]["Sexo estudiante"] = actualizarsexo
                    break
                elif modificar == 3:
                    actualizargrado = int(input("Ingrese nuevo valor trabajadas: "))
                    infoestudiantes[buscarid]["Grado estudiante"] = actualizargrado
                    break
                else:
                    print("Ingrese un numero valido")
            else:
                ("ID NO ENCONTRADO")
            
            input("---> Presione ENTER para continuar")


    def buscar():
        while True:
            infoestudiantes = {}
            buscarid = input("Ingrese el id del empleado que desea buscar: ")
            if buscarid in infoestudiantes:
                print("ID ENCONTRADO")
                nombre = infoestudiantes[buscarid]["Nombre estudiante"]
                sexo = infoestudiantes[buscarid]["Sexo estudiante"]
                grado = infoestudiantes[buscarid]["Grado estudiante"]

                print("-----DATOS ESTUDIANTE----")
                print("Los datos del estudiante son: ")
                print(f"ID estudiante: {buscarid}")
                print(f"Nombre estudiante: {nombre}")
                print(f"Sexo estudiante: {sexo}")
                print(f"Grado estudiante: {grado}")
                break
            else:
                ("Empleado no encontrado")
    input("---> Presione ENTER para continuar")

    def eliminar():
            infoestudiantes = {}
            while True:
                buscarid = input("Ingrese el id del empleado que desea eliminar : ")
                if buscarid in infoestudiantes:
                    infoestudiantes.pop(buscarid)
                    print(f"ID ELIMINADO,se elimino el id : {buscarid}")
                    break
                print("El id ingresado no existe ingrese de nuevo ")
                
            input("---> Presione ENTER para continuar")

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
        break