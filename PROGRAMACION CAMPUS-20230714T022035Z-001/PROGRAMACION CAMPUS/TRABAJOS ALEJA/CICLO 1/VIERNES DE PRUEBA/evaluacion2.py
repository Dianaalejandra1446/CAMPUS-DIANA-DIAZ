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

CAMPUS LADS
SOFTWARE REVIEW – CICLO I Rev 01/06/2023
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
        opcion = int(input("Selecciona una opcion: "))
        return opcion
nominaempleado = {}
idlista = []
nombrelista =[]
valorhoralista =[]
horalista =[]



def agregar_empleado():
    
    id = int(input("Ingrese el id del empleado: "))
    idlista.append(id)

    nombre = input("Ingrese el nombre del emepleado: ")
    nombrelista.append(nombre)

    
    while True:
        valorhora = int(input("Ingrese el valor de la hora trabajada: "))
        if valorhora < 8000 or valorhora > 150000:
            input("Ingresa un valor valido:")
        else:
            valorhoralista.append(valorhora)
            break
        
    
    while True:
        horastrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        if horastrabajadas < 1 or horastrabajadas > 160:
            print("La cantidad de horas solo va de  1 a 160 horas")
            print("Ingresa un valor valido:")
        else:
            horalista.append(horastrabajadas)
            break
    print("- "*30)
    print(f"El id del empleado es {id}")
    print(f"El nombre del empleado es {nombre}")
    print(f"El valor de la hora del empleado es {valorhora}")
    print(f"Las horas trabajadas son {horastrabajadas}")
    print("-"*30)   

def modificar_empleado():
    print("MODIFICAR AL EMPLEADO:")
    buscarid = int(input("Ingrese el id del empleado que desea modificar: "))
    while True:
        if buscarid in idlista:
            lugarid =idlista.index(buscarid)  
            print("ID del empleado encontrado")
            break
        else:

            input("Ingresa un ID valido")
           
    
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
            nuevonombre = input("Ingrese el nuevo nombre del empleado: ")
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
    while True:
        buscarid = int(input("Ingrese el id del empleado que desea buscar: "))
        if buscarid in idlista:
            lugarid =idlista.index(buscarid)  
            print("ID del empleado encontrado")
            print(f"El nombre del empleado con el id {buscarid} es {nombrelista[lugarid]}")
            print(f"La horas trabajadas del empleado con el id {buscarid} es {horalista[lugarid]}")
            print(f"El valor por hora del empleado con el id {buscarid} es {valorhoralista[lugarid]}")
            break
        else:
            print("El empleado no ha sido ingresado")

def eliminar_empleado():
    print("Eliminar empleado: ")
    lugarid=0
    buscarideliminar = int(input("Ingrese el id del empleado que desea eliminar: "))
    while True:
        if buscarideliminar in idlista:
            lugarid =idlista.index(buscarideliminar)  
            print("ID del empleado encontrado") 
            idlista.pop(lugarid)
            nombrelista.pop(lugarid)
            valorhoralista.pop(lugarid)
            horalista.pop(lugarid)
            break
    print("Ya se elimino el empleado")
  

def lista_empleados():
    """5. Listar Empleados: Esta opción permite mostrar los empleados con su información (id, nombre, horas y
valor de la hora trabajada), debe permitir paginación, esto es, se muestran los primeros 5 empleados,
luego para y muestra un mensaje para que el usuario decida si desea seguir viendo o volver al menú. Si
desea seguir viendo, le muestra los siguientes 5 empleados y así sucesivamente hasta que no haya más
empleados o la persona no desee seguir viendo."""
    contador = 4
    for empleado in range(len(idlista)):
        print("#"*40)
        print("LISTA EMPLEADOS ")
        print("#"*40)
        print(f"El nombre del empleado es {nombrelista[empleado]}")
        print(f"El valor de la hora del empleado es {valorhoralista[empleado]}")
        print(f"Las horas trabajadas del empleado son {horalista[empleado]}")
        if empleado == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                contador += 5
                continue
            elif opcion == 2:
                break

def lista_nomina():
    print("NOMINA EMPLEADO: ")
    while True:
        buscarid = int(input("Ingrese el id del empleado que desea ver su nomina buscar: "))
        if buscarid in idlista:
            lugarid =idlista.index(buscarid)
            break
    
    sueldobruto = horalista[lugarid] * horalista[lugarid]
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    auxilio = 0
    if sueldobruto <= 1160000:
        print("Merecedor subsidio de transporte")
        auxilio = 140606
    sueldoneto = (sueldobruto + auxilio )- descuento

    print(f"La nomina del empleado {nombrelista[buscarid]}")
    print(f"Sueldo bruto: {sueldobruto}")
    print(f"Valor eps: {eps}")
    print(f"Valor pension: {pension}")
    print(f"Valor auxilio: {auxilio}")
    print(f"Sueldo neto: {sueldoneto}")

def lista_total_nomina():
    """7. Listar nómina de todos los empleados: Esta opción permite mostrar la nómina de todos los empleados.
El listado debe estar paginado cada 5 empleados. El calculo de la nómina de cada empleado es el mismo
que en la opción 6."""
    contador = 4
    for empleado in range(len(idlista)):
        sueldobruto = horalista[empleado] * horalista[empleado]
        eps = sueldobruto * 0.04
        pension = sueldobruto * 0.04
        descuento = (eps + pension)
        auxilio = 0
        if sueldobruto <= 1160000:
            print("Merecedor subsidio de transporte")
            auxilio = 140606
        sueldoneto = (sueldobruto + auxilio )- descuento
       

        print("#"*40)
        print(f"La nomina de los empleados {nominaempleado}")
        print(f"Sueldo bruto: {sueldobruto}")
        print(f"Valor eps: {eps}")
        print(f"Valor pension: {pension}")
        print(f"Valor auxilio: {auxilio}")
        print(f"Sueldo neto: {sueldoneto}")
        if empleado == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            while True:
                opcion = int(input("OPCION: "))
                if opcion != 1 or opcion != 2:
                    print("Elige una opcion entre 1 o dos solamente")
                if opcion == 1:
                    contador += 5
                    continue
                elif opcion == 2:
                    break

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
         lista_empleados()
    elif opcion == 6:
        lista_nomina()
    elif opcion == 7:
        lista_total_nomina()
    elif opcion == 8:
        print("\n -----Saliste de la base de datos de los empleados---")
        break
