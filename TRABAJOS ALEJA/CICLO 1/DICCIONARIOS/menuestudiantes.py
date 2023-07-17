import json
#PROGRAMA PRINCIPAl (debajo de las funciones de carga) 
ruta = "CICLO 1\JSON\instituto.json"
dicdata = {}
"""cargarInfo(ruta,dicdata)"""

def cargarInfo():
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
    return dic

def menu():
    print("-"*40)
    print("Menu")
    print("--Base de datos Colegio--")
    print("-"*40)
    print("1.Estudiantes ")
    print("2.Notas")
    print("3.Reportes")
    print("4.Salir")
    while True:
        opcion = leerInt("Ingrese una opcion de menu que va utilizar: ")
        if opcion <1 or opcion > 4:
            print("Digita una opcion valida")
            continue
        return opcion
def menuestudiantes():
    print("1. Agregar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Salir")
    while True:
        opcion = leerInt("Ingrese una opcion de menu que va utilizar: ")
        if opcion <1 or opcion > 5:
            print("Digita una opcion valida")
            continue
        break
    while True:
        if opcion == 1:
            agregar()
        if opcion == 2:
            modificar()
        if opcion == 3:
            eliminar()
        if opcion== 4:
            buscar()
        if opcion == 5:
            print("Haz salido de menu estudiantes")
            break


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")

def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip() == "":
                print("Error! Ingrese el nombre valido.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError as e:
            print("Error! Hay que ingresar el nombre.")

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")


def cargar_estudiantes (infoestudiantes):
    with open(ruta, "w") as archivo:
        json.dump(infoestudiantes, archivo)

def agregar():
    infoestudiantes = cargarInfo()
    while True:
        grado = input("Ingrese el grado del estudiante")
        if not (grado in infoestudiantes):
            infoestudiantes[grado] = {}
        while True:
            id = int(input("Ingrese id del estudiante: "))
            if id in infoestudiantes[grado]:
                print("El id ya existe digita uno nuevo")
                continue
            break
        infoestudiantes[grado][id] = {}
        print(f"El id del estudiante es {id}")

        nombreEstu = input("Ingrese el nombre del estudiante: ")
        infoestudiantes[grado][id]["Nombre estudiante"] = nombreEstu
        print(f"El nombre del estudiante es {nombreEstu}")

        sexo = input("Ingrese el sexo del estudiante F o M")
        infoestudiantes[grado][id]["Sexo estudiante"] = sexo.upper
        print(f"El sexo del estudiante es {sexo}")

        while True:
            agregarotro = input("Desea agregar otro estudiante? si/no")
            if agregarotro == "si":
                opcion = False
                break
            elif agregarotro == "no":
                opcion = True
                break
            else:
                print("digite un opcion valida")
        if opcion:
            break

    cargar_estudiantes(infoestudiantes)
    input("---> Presione ENTER para continuar")




def modificar():
    infoestudiantes = cargarInfo()
    print("Modificar Estudiante: ")
    print("----Seleccione el numero de lo que quiere modificar---- ")
    print("\n 1.Modificar nombre \n 2.Modificar sexo \n 3.Modicar grado")

    while True:
        opcion = leerInt("Ingrese una opcion: ")
        if opcion <1 or opcion > 3:
            print("Digita una opcion valida")
            continue
        break

    while True:
        buscarid = input("Ingrese el id del estudiante que desea modificar: ")
        for x in infoestudiantes.keys():
            if buscarid in infoestudiantes[x]:
                grado = x
                validacion = True
        if validacion :
            print("ID ENCONTRADO")
            break
        else:
            print("ID NO ENCONTRADO")
        
    while True:
        if opcion == 1:
            nuevonombre= input("Ingrese el nuevo nombre: ")
            infoestudiantes[grado][buscarid]["Nombre estudiante"] = nuevonombre
            break
        elif modificar == 2:
            actualizarsexo = input("Ingrese nuevo sexo del estudiante: ")
            infoestudiantes[grado][buscarid]["Sexo estudiante"] = actualizarsexo
            break
        elif opcion == 3:
            actualizargrado = int(input("Ingrese nuevo valor trabajadas: "))
            infoestudiantes[grado][buscarid]["Grado estudiante"] = actualizargrado
            break
    
    cargar_estudiantes(infoestudiantes)
    input("---> Presione ENTER para continuar")


def buscar():
    infoestudiantes = cargarInfo()

    while True:
        buscarid = input("Ingrese el id del estudiante que desea buscar: ")
        for x in infoestudiantes.keys():
            if buscarid in infoestudiantes[x]:
                grado = x
                validacion = True
        if validacion :
            print("ID ENCONTRADO")
            break
        else:
            print("ID NO ENCONTRADO")

    nombre = infoestudiantes[grado][buscarid]["Nombre estudiante"]
    sexo = infoestudiantes[grado][buscarid]["Sexo estudiante"]
    grado = infoestudiantes[grado][buscarid]["Grado estudiante"]

    print("-----DATOS ESTUDIANTE----")
    print("Los datos del estudiante son: ")
    print(f"ID estudiante: {buscarid}")
    print(f"Nombre estudiante: {nombre}")
    print(f"Sexo estudiante: {sexo}")
    print(f"Grado estudiante: {grado}")
    infoestudiantes = {}#LIBERA DATOS DE LA MEMORIA PARA MEJOR FUNCIONAMIENTO
    input("---> Presione ENTER para continuar")

def eliminar():
    infoestudiantes = cargarInfo()
    while True:
        buscarid = input("Ingrese el id del empleado que desea eliminar : ")
        if buscarid in infoestudiantes:
            infoestudiantes.pop(buscarid)
            print(f"ID ELIMINADO,se elimino el id : {buscarid}")
            break
        print("El id ingresado no existe ingrese de nuevo ")
        infoestudiantes = {}
    input("---> Presione ENTER para continuar")

def notas():
        """El programa debe registrar las notas de los estudiantes. El software debe
permitir al docente ingresar el grupo al cual desea ingresar notas, luego de
esto el software listará los estudiantes por orden alfabético y por cada uno el
docente podrá ingresar las notas de dicho estudiantes (cada estudiante puede
tener diferentes cantidad de notas)"""
infoestudiantes = cargarInfo()
contador = 0
while True:
    gradoasignar = input("Ingrese el grado para asignar la nota")
    if not (grado in infoestudiantes):


#EL NUMERO DE NOTAS INGRESADA
numeronotas = int(input("Ingrese la cantidad de notas"))
for cantidad in numeronotas:
    cantidad = int(input("Ingrese la nota del estudiante: "))
    if cantidad == numeronotas:
        contador =+ numeronotas
        break
    else:
        print("Grado NO ENCONTRADO")

while True:
    id = int(input("Ingrese id del estudiante: "))
    if id in infoestudiantes[grado]:
        print("")
        continue
    break
infoestudiantes[grado][id] = {}
print(f"El id del estudiante es {id}")

for x in infoestudiantes[grado]:


notas = []
nombre.sort()#sort o sorted
notas.append(notaingresada)

cargar_estudiantes(infoestudiantes)
input("---> Presione ENTER para continuar")

def reportes():
        """Listado de notas promedios por grado. Este listado muestra los id,
nombre y nota promedio de los estudiantes

▪ Terna de excelencia por grado. El programa mostrará los 5 mejores
estudiantes de un grado ordenados descendentemente por nota
promedio . Se muestra el nombre y la nota promedio del estudiante.

▪ Terma de excelencia del colegio. El programa muestra un listado
parecido al anterior pero con los 5 mejores estudiantes de todo el
colegio. En el listado aparece el nombre del estudiante, el grado y su
nota promedio."""
print("*"*30)
print("MENU REPORTE ESTUDIANTIL: ")
print("*"*30)
print("----Seleccione el numero de lo que quiere modificar---- ")
print("\n 1.Promedios por grado \n 2.Excelencia por grado \n 3.Excelencia colegio")

while True:
    opcion = leerInt("Ingrese una opcion: ")
    if opcion <1 or opcion > 3:
        print("Digita una opcion valida")
        continue
    break

while True:
    if opcion == 1:
        pass
        break
    elif opcion == 2:
        pass
        break
    elif opcion == 3:
        pass
        break
#MENUS
while True:
    op = menu()
    if op == "1":
        menuestudiantes()
    elif op == "2":
        notas()
    elif op == "3":
        reportes()
    elif op == "4":
        print("Gracias por usar este programa")
        input("Presione cualquier tecla para salir...")
        break
