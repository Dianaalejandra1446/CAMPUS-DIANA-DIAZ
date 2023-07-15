"""*** NOMINA ACME ***
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

CAMPUS LADS
SOFTWARE REVIEW – CICLO I Rev 01/06/2023
Estructura Repetitivas WHILE – Validación Errores Trainer Ing.
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
el programa.
"""
def menu():
        print("\n--------------")
        print(" MENU ")
        print("----------------\n")
        print("1.Agregar empleado")
        print("2.Modificar empleado")
        print("3.Buscar empleado")
        print("4.Eliminar empleado")
        print("4.Lista de empleados")
        print("5.Lista nomina de un empleado")
        print("6.Lista nomina de todos los empleados")
        print("7.Salir")
        print(">> Escoja una opción (1-8)?")

nominaacme =[[idlista]
            [nombrelista]
            [valorhoralista]
            [horalista]
            [listaemple]
            [listanomina]
            [listatotalnomina]]
idlista = []
nombrelista =[]
valorhoralista =[]
horalista =[]
listaemple = []
listanomina =[]
listatotalnomina =[]

def agregar_empleado():
    
    id = int(input("Ingrese el id del empleado: "))
    idlista.append(id)

    nombre = input("Ingrese el nombre del emepleado: ")
    nombrelista.append(nombre)

    valorhora = int(("Ingrese el valor de la hora trabajada"))
    if valorhora <= 8000 and valorhora >= 150000:
        valorhoralista.append(valorhora)
        print(valorhora)
    else:
         print("Ingresa un valor de hora adecuado")

    horastrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

    if horastrabajadas < 1 or horastrabajadas > 160:
         print("La cantidad de horas solo va de  1 a 160 horas")
         print("Ingresa un valor valido:")
         return
    elif horastrabajadas <= 1 or horastrabajadas >= 160:
         horalista.append(horastrabajadas)
         print(f"Sus horas trabajadas son de:{horastrabajadas} ")


def modificar_empleado():
    print("MODIFICAR AL EMPLEADO:")
    buscarid = int(input("Ingrese el id del empleado que desea modificar: "))
    while True:
        if buscarid in idlista:
            lugarid =idlista.index(buscarid)  
            print("ID del empleado encontrado")
            break
        else:
            print("Ingresa un ID valido")
    
    nombre = nombrelista[lugarid]
    print("*"*35)
    print("\n ACTUALIZAR DATOS")
    print ("1.Cambiar nombre")
    print("2.Cambiar horas trabajadas")
    print("3.Cambiar valor hora")
    while True:
        try:
         ingresado = int(input("Lo que desea buscar es: "))
         if ingresado < 1 or ingresado > 3:
              print("Ingrese una opcion valida")
              return
         else:
              print(f"Ingresaste la opcion {ingresado}")
              break
        except ValueError:
            print("Ingresa un valor valido")
    
    while True:
        if ingresado == 1:
            nuevonombre = input("Ingrese el nuevo nombre del empleado")
            nombrelista[buscarid] = nuevonombre
            print(f"Su nuevo nombre es {nuevonombre}")
        elif ingresado == 2:
            nuevahora = int(input("Ingrese las nuevas horas trabajadas"))
            nombrelista[buscarid] = nuevahora
            print(f"Su nuevas horas trabajadas son de {nuevahora}")
        elif ingresado == 3:
            nuevovalor = int(input("Ingrese el nuevo valor de la hora"))
            nombrelista[buscarid] = nuevovalor
            print(f"Su nuevo valor de la hora es: {nuevovalor}")
        else:
            break
            input("--> Presione cualquier tecla para volver al menu")

def buscar_empleado():
    print("BUSCAR AL EMPLEADO:")
    buscarid = int(input("Ingrese el id del empleado que desea buscar: "))
    while True:
        if buscarid in idlista:
            lugarid =idlista.index(buscarid)  
            print("ID del empleado encontrado")
            print(f"El nombre del empleado con el id {buscarid} es {nombre}")
            print(f"La horas trabajadas del empleado con el id {buscarid} es {horastrabajadas}")
            print(f"El valor por hora del empleado con el id {buscarid} es {valorhora}")
            break
        else:
            print("El empleado no ha sido ingresado")

def eliminar_empleado():
    
    """4. Eliminar empleado: Esta opción permite eliminar a un empleado por su id. Si borra al empleado, muestra
un mensaje que ha sido eliminado y si no, muestra un mensaje de que no se eliminó el empleado."""
def lista_empleados():
    pass
def lista_nomina():
    pass
def lista_total_nomina():
    pass

#ELEGIR MENU
while True:
    opcion = menu()

    if opcion == 1:
        agregar_empleado()
    elif opcion == 2:
        modificar_empleado()
    elif opcion == 3:
        buscar_empleado()
    elif opcion == 4:
        eliminar_empleado()
    elif opcion == 5:
        print("\n -----Saliste de la base de datos de los empleados---")
        break