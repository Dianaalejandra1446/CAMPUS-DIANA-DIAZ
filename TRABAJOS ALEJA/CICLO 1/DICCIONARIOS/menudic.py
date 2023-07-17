"""INTRODUCCIÓN
Resuelva los siguientes enunciados en Python validando la entrada del usuario y usando diccionarios.

ENUNCIADO
La empresa ACME desea que le construya un programa para gestionar la nómina de sus empleados. Después
de recoger los requerimientos se llegó a la decisión de gestionar los empleados y sus nóminas a través del
siguiente menú.

*** NOMINA ACME ***
MENU
1- Agregar empleado
2- Modificar empleado
3- Buscar empleado
4- Eliminar empleado
5- Listar empleados
6- Listar nómina de un empleado
7- Listar nómina de todos los empleados
8- Salir
>> Escoja una opción (1-8)?

1. Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora.
2. Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de
empleado.
3. Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la
información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado
4. Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado.
5. Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo.
Estructura de datos - Diccionarios Trainer Ing.
Carlos H. Rueda C.
6. Listar la nómina de un empleado: Esta opción permite mostrar la nómina de un empleado buscado por
su ID. El salario bruto se calcula como el valor de la hora por la cantidad de horas trabajadas. Si gana
menos del salario mínimo legal vigente en Colombia 2023 (por favor consulte el dato) se le debe da
subsidio de transporte. Se le debe descontar el valor de la eps y pensión correspondiente al 4% cada uno
y el salario Neto es la suma del salario bruto, el auxilio menos los descuentos.
El menú debe mostrar los datos del empleado y los datos de la nómina.
7. Listar nómina de todos los empleados: Esta opción permite mostrar la nómina de todos los empleados.
El listado debe estar paginado cada 5 empleados. El calculo de la nómina de cada empleado es el mismo
que en la opción 6.
8. Salir: Esta opción sale del programa, pero antes le pregunta al usuario si desea salir de la aplicación.
Sino no desea, vuelve al menú. Si desea salir de la aplicación muestra un mensaje de despedida y termina
el programa."""
nominacme = {}

#PROGRAMA GENERAL
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

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

#MENU ELEGIR PROGRANA
def menu():
        print("\n---------------")
        print(" NOMINA ACME MENU: ")
        print("----------------\n")
        print("1.Agregar empleado ")
        print("2.Modificar empleado ")
        print("3.Buscar empleado ")
        print("4.Eliminar empleado ")
        print("5.Listar empleados ")
        print("6.Listar nomina de un empleado ")
        print("7.Listar nomina de todos los empleados")
        print("8.Salir ")
        print(">> Escoja una opcion (1-8)?")
        elegirop = leerInt ("\n>> Opcion (1 a 8)? ")
        if elegirop < 1 or elegirop > 8:
            msgError("Ingrese una opcion valida")
        return elegirop

def Agregar_empleado():
    """1. Agregar empleado: Esta opción permite adicionar un empleado con su id, nombre, horas trabajadas y
valor de la hora. Los empleados pueden trabajar entre 1 a 160 Horas. Y el valor de la hora puede estar
entre $8,000 y $150,000 pesos la hora."""
    agregarempleado = {}

    id = input("Ingrese el id del empleado: ")
    agregarempleado ["id"] = id
    print(f"Id empleado: {id}")

    nombre = input("Ingrese el nombre de empleado: ")
    agregarempleado["nombre"] = nombre
    print(f"Nombre empleado: {nombre}")

    horas = int(input("Ingrese horas trabajadas: "))
    agregarempleado["Horas trabajadas"] = horas
    while True:
            if horas < 1 or horas > 160:
                print("Ingrese una hora valida")
                return horas
            else:
                break
    print(f"Horas trabajadas: {horas}")

    valorhora = int(input("Ingrese el valor de la hora trabajada: "))
    agregarempleado["Valor hora"] = valorhora
    while True:
        if valorhora < 8000 or valorhora >150000:
            print("Ingrese un valor de hora adecuado")
            return horas
        else:
            break
    print(f"Valor horas trabajadas {valorhora}")
    print("LOS VALORES DEL NUEVO EMPLEADO SON: ")
    agregartodo = agregarempleado.items()
    print(agregarempleado)

def Modificar_empleado():
    """2. Modificar empleado: Esta opción permite cambiar cualquiera de los datos del empleado, menos el id de empleado."""
    print("Modificar empleado: ")
    print("----Seleccione el numero de lo que quiere modificar---- ")
    print("\n 1.Modificar nombre \n 2.Modificar horas \n 3.Modicar valor hora")
    buscarid = input("Ingrese el id del empleado que desea modificar: ")
    while True:
        if buscarid in "id":
            print("ID ENCONTRADO")
            modificar = int(input("Ingrese un numero: "))
            if modificar == 1:
                nombrenuevo = input("Ingrese el nuevo nombre: ")
                agregarempleado ["nombre"] = nombrenuevo
            elif modificar == 2:
                nuevahora = int(input("Ingrese las nuevas horas trabajadas: "))
                agregarempleado ["Horas trabajadas"] = nuevahora
            elif modificar == 3:
                nuevovalorh = int(input("Ingrese nuevo valor trabajadas: "))
                agregarempleado ["Valor hora"] = nuevovalorh
            else:
                print("Ingrese un numero valido")
                return modificar
        else:
            ("ID NO ENCONTRADO")

def Buscar_empleado():
    """3. Buscar empleado: Esta opción permite buscar un empleado por su id, si lo encuentra, muestra la información de este y si no, muestra un mensaje de que el empleado no ha sido ingresado"""
    while True:
        if buscarid in "id":
            print("ID ENCONTRADO")
def Eliminar_empleado():
    pass
def Listar_empleados():
    pass
def nómina_empleado():
    pass
def nómina_todos():
    pass 

#Validacion menu:
while True:
    elegirop = menu()

    if elegirop == 1:
        Agregar_empleado()
    elif elegirop == 2:
        Modificar_empleado()
    elif elegirop == 3:
        Buscar_empleado()
    elif elegirop == 4:
        Eliminar_empleado()
    elif elegirop == 5:
        Listar_empleados()
    elif elegirop == 6:
        nómina_empleado()
    elif elegirop == 7:
        nómina_todos()