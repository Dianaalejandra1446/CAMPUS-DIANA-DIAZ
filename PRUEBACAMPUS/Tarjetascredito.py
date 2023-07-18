import json
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

ruta = "PRUEBACAMPUS/Tarjetascredito.json"
datoscliente = {}



def cargar_clientes (datoscliente):
    with open(ruta, "w") as archivo:
        json.dump(datoscliente, archivo)

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("-"*75)
            print("Ingrese un numero entero valido")

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

def menu():
    print("-"*50)
    print("###### BIENVENIDO AL MENU TARJETAS CREDITO ACME ######")
    print("-"*50)
    print("1.Añadir: ")
    print("2.Modificar: ")
    print("3.Eliminar: ")
    print("4.Reportes ")
    print("5.Salir ")
    print(">> Escoja una opcion (1-5)?")
    elegirop = leerInt ("\n>> Opcion (1 a 5)? ")
    if elegirop < 1 or elegirop > 5:
        msgError("Ingrese una opcion valida")
    return elegirop

def Agregar():

    #submenu
    print("\n MENU AÑADIR")
    print("*"*40)
    print("\n 1.Añadir cliente del banco: ")
    print("\n2.Añadir informacion tarjeta ")
    cargar_clientes = cargarInfo
    while True:

        opcionsubmenu = leerInt("Seleccion lo que desea añadir: ")
        if opcionsubmenu < 1 or opcionsubmenu > 2:
            print("Ingrese un valor valido")
            continue
        break
    if opcionsubmenu == 1:
        id = leerInt("Ingrese el numero del id: ")
        datoscliente[id] = {}
        print("Id ingresado ",id)
    
        print("Añadir nuevo cliente")
        nombre = leerString("Ingrese nombre del cliente: ")
        datoscliente[id]["Nombre cliente"] = nombre

        cedula = leerString("Ingrese el numero de cedula: ")
        datoscliente[id]["N* cedula"] = cedula

        numero = leerInt("Ingrese su numero de telefono: ")
        datoscliente[id]["Numero telefono"] = numero

        sexo = leerString("Ingrese su sexo")
        datoscliente[id]["Sexo"] = sexo

        print("#"*40)
        print(f"Nuevo cliente banco ingresado: {nombre}")
        print("Numero cedula ingresado", cedula)
        print("Numero telefono ingresado", numero)
        print("Sexo ingresado: ",sexo)
        print("#"*40)


    elif opcionsubmenu == 2:
        print("Añadir informacion tarjeta: ")
        
        id = leerInt("Ingrese el numero del id: ")
        datoscliente[id] = {}
        print("Id ingresado ",id)

        nombredueño = leerString("Ingrese el numero propietaro de la tarjeta: ")
        datoscliente[id]["Nombre dueño"] = nombredueño

        numeroTar = leerInt("Ingrese el numero de tarjeta de credito: ")
        datoscliente[id]["Numero tarjeta"] = numeroTar
        print("Numero Tarjeta ingresado",numeroTar)

        mes = leerString("Ingrese el mes de validez: ")
        datoscliente[id]["Mes validez"] = mes
        print("Numero mes ingresado",mes)

        año = leerInt("Ingrese el año de validez: ")
        datoscliente[id]["Año validez"] = año
        print("Año ingresado:",año)

        codigo = leerInt("Ingrese su codigo de verificacion: ")
        datoscliente[id]["Codigo verificacion"] = codigo
        if codigo < 100 or codigo < 999:
            print("Ingrese un codigo valido")
        else:
            print("Codigo ingresado",codigo)

        while True:
            tipoTar = leerString("Seleccione su tipo de tarjeta de credito: //master card // visa // american express: ")
            datoscliente[id]["Tipo tarjeta"] = tipoTar
            if tipoTar == "master card" or tipoTar =="visa" or tipoTar == "american express":
                print("Tipo de tarjeta ingresado", tipoTar)
                break
            else:
                print("Tipo de tarjeta invalido")
                continue
        input("---> Presione ENTER para continuar")
1
def Modificar():
    cargar_clientes = cargarInfo
    print("MODIFICAR")
    print("-"*40)
    print("\n 1.Modificar Tipo \n 2.Modificar numero \n 3.Modicar mes \n 4.Modificar año \n 5.Modificar codigo verificacion")

    while True:
        buscaridmodi = leerInt("Ingrese el id de la tarjeta que desea modificar: ")
        if buscaridmodi in datoscliente:
            print("ID ENCONTRADO")
            break
        else:
            ("ID NO ENCONTRADO")

            modificar = int(input("Ingrese un numero: "))
            if modificar == 1:
                tiponuevo = input("Ingrese el nuevo tipo de tarjeta: ")
                datoscliente[buscaridmodi]["Tipo tarjeta"] = tiponuevo
                break
            elif modificar == 2:
                nuevonumero = int(input("Ingrese el nuevo numero: "))
                datoscliente[buscaridmodi]["Numero tarjeta"] = nuevonumero
                break
            elif modificar == 3:
                nuevomes = leerString("Ingrese nuevo valor del mes: ")
                datoscliente[buscaridmodi]["Mes validez"] = nuevomes
                break
            elif modificar == 4:
                nuevoaño = int(input("Ingrese su nuevo año"))
                datoscliente[buscaridmodi]["Año validez"] = nuevoaño
            elif modificar == 5:
                nuevocodigover = int(input("Ingrese nuevo codigo de verificacion: "))
                datoscliente[buscaridmodi]["Codigo verificacion"] = nuevocodigover
                break
            else:
                print("Ingrese un numero valido")
                cargar_clientes (datoscliente)

    input("---> Presione ENTER para continuar")
def Eliminar():
        while True:
            buscarid = input("Ingrese el id del cliente o tarjeta que desea eliminar : ")
            if buscarid in datoscliente:
                datoscliente.pop(buscarid)
                print(f"ID ELIMINADO,se elimino el id : {buscarid}")
                break
            print("El id ingresado no existe ingrese de nuevo ")
        input("---> Presione ENTER para continuar")

def Reportes():
    cargar_clientes = cargarInfo

#submenu
    print("\n MENU REPORTES")
    print("*"*40)
    print("\n 1.Tarjetas credito de un cliente: ")
    print("\n2.Informacion Tarjeta credito")
    print("\n3.Listado tarjetas credito")
    print("\n4.Lista de clientes con tarjeta de credito")
    print("\n5.Cantidad de tarjetas de cierto tipo")


    while True:
        opcionsubmenu2 = leerInt("Seleccion lo que desea añadir: ")   
        if opcionsubmenu2 < 1 or opcionsubmenu2 > 2:
            print("Ingrese un valor valido")
            continue
        break
    if opcionsubmenu2 == 1:
        print("Tarjetas credito del cliente")
        while True:
            buscarid = leerInt("Ingrese numero del id a buscar: ")
            if buscarid in datoscliente:
                print("ID ENCONTRADO")
                
                nombre = datoscliente[buscarid]["Nombre cliente"]
                numeroTar = datoscliente[buscarid]["Numero tarjeta"]
                tipoTar = datoscliente[buscarid]["Tipo tarjeta"]
                mes = datoscliente[buscarid]["Mes validez"]
                año = datoscliente[buscarid]["Año validez"]
                codigo= datoscliente[buscarid]["Codigo verificacion"]

                print("-----DATOS CLIENTE----")
                print("Los datos del estudiante son: ")
                print(f"El id del cliente es: {buscarid}")
                print(f"El numero de tarjeta del cliente es: {numeroTar}")
                print(f"El tipo de tarjeta del cliente es: {tipoTar}")
                print(f"El mes de validez es: {mes}")
                print(f"El año del cliente es {año}")
                print(f"El codigo de verificacion es: {codigo}")

                print(f"Nombre estudiante: {nombre}")

                break
            else:
                print("ID NO ENCONTRADO")
                

                input("---> Presione ENTER para continuar")

    elif opcionsubmenu2 == 2:
        print("---Informacion tarjeta de credito---")
        while True:
                buscartarjeta = leerInt("Ingrese el numero de la tarjeta de credito")
                if buscartarjeta in datoscliente:
                    print("TARJETA ENCONTRADA")
                    print("DATOS DE LA TARJETA DEL CLIENTE: ")
                    print("-"*40)
                    datoscliente[buscartarjeta]["Numero tarjeta"] = numeroTar
                    datoscliente[buscartarjeta]["Tipo tarjeta"] = tipoTar
                    datoscliente[buscartarjeta]["Mes validez"] = mes
                    datoscliente[buscartarjeta]["Año validez"] = año
                    datoscliente[buscartarjeta]["Codigo verificacion"] = codigo
                    print("-"*40)
                    print("DATOS DEL CLIENTE")
                    datoscliente[buscartarjeta]["Nombre dueño"] = nombre
                else:
                    print("TARJETA NO ENCONTRADA")
    elif opcionsubmenu2 == 3:
        contador = 0
        indicador = 0
        print("---Listado tarjetas credito---")
        while True:
            for tarjeta in datoscliente.keys:
                print("#"*40)
                print("***lista tarjetas*** ")
                print("#"*40)

                idencontrado = tarjeta
                nombretarjeta = datoscliente[tarjeta]["Nombre dueño"]
                numerotarje = datoscliente[tarjeta]["Numero tarjeta"]
                fechaven = datoscliente[tarjeta]["Mes validez"]["Año validez"]
                tipo = datoscliente[tarjeta]["Tipo tarjeta"]

                print("---DATOS TARJETAS----")
                print("Los datos de la tarjeta son:")
                print("El id del empleado es ",idencontrado)
                print("El nombre el cliente es ",nombretarjeta)
                print("El numero de tarjeta es ", numerotarje)
                print("La fecha de vencimiento es", fechaven)
                print("El tipo de tarjeta es ",tipo)

                if indicador == contador:
                    print("Quieres ver otra tarjeta? ")
                    print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
                    opcion = int(input("OPCION: "))
                    if opcion == 1:
                        contador += 1
                        continue
                    elif opcion == 2:
                        break
                indicador += 1
            input("---> Presione ENTER para continuar")
    elif opcionsubmenu2 == 4:
        contador2 = 0
        indicador2 = 0
        print("-"*30)
        print("LISTADO CLIENTES TARJETA CREDITO")
        print("-"*30)
        while True:
            for cliente in datoscliente.keys:
                    print("#"*40)
                    print("***lista clientes*** ")
                    print("#"*40)

                    idcliente = cliente
                    cedula = datoscliente[cliente]["N* cedula"]
                    nombrecliente = datoscliente [cliente]["Nombre cliente"]
                    telefono = datoscliente[cliente]["Numero telefono"]

                    print("---DATOS CLIENTES---")
                    print("\n")
                    print(f"El id del cliente es {idcliente}")
                    print(f"La cedula del cliente es {cedula}")
                    print(f"El nombre del cliente es {nombrecliente}")
                    print(f"El numero del cliente es {telefono}")

                    if indicador2 == contador2:
                        print("Quieres ver otra tarjeta? ")
                        print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
                        opcion = int(input("OPCION: "))
                        if opcion == 1:
                            contador2 += 1
                            continue
                        elif opcion == 2:
                            break
                    indicador2 += 1
    
    elif opcionsubmenu2 == 5:
        contador3 = 0
        while True:
            for tipo in tipoTar:
                contador += 1
                print("El numero de tipo de tarjetas son ",contador3)
            cargar_clientes (datoscliente)

        
while True:
    opmenu = menu()
    if opmenu == 1:
        Agregar()
    elif opmenu == 2:
        Modificar()
    elif opmenu == 3:
        Eliminar()
    elif opmenu == 4:
        Reportes()
    elif opmenu == 5:
        print("Se ha cerrado el programa")
        break



