def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("-"*75)
            print("Ingrese un numero entero valido ")

def leerString(msg):
    while True:
        try:
            n = int(input(msg))
            if n.strip() == "":
                print("Error ingrese un nombre valido! ")
                input("Digite cualquier tecla para continuar")
                continue
            return n
        except ValueError as e:
            print("-"*75)
            print("Error! Hay que ingresar un nombre. ")

def lista_compras():
    datas = {}
    return datas

def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("----> Presione ENTER para continuar")

def menu():
    print("-"*30)
    print("MENU <<< SushimeMo >>> STORE\n")
    print('|1.Registrar compra y descuentos       |')
    print('|2.Modificar comprador                 |')
    print('|3.Modificar compra                    |')
    print('|4.Buscar compra y comprador           |')
    print('|5.Eliminar compra y aplicar devolucion|')
    print('|6.Lista total de compradores          |')
    print('|7.Lista total de compras              |')
    print('>>Escoja una opcion (1-8)?')
    print("-"*30)
    elegirop = leerInt(">>> Opcion (1 a 8)?")
    if elegirop < 1 or elegirop > 8:
        msgError("--Ingrese una opcion valida--")

def Agregar(datas):
    mujer = [{
        'metro shirt': '15010059W00O0O302',
        'now blouse': '1502004CW00PQN301',
        'Trynity blouse': '1502004DW00Q3D301',
        'Hebo top':'1504000AJ005NO308',
        'Overside T-shirt':'3G010018C003EO307'
        'Long ginnie pencil dress':'1101034VW00F6N401'
    }]
    hombre = []
    nombre = leerString(input('Ingrese su nombre'))
    fecha = leerString(input('Ingrese la fecha de compra'))
    id = leerInt(input('Ingrese el numero id de compra'))
    numero = leerInt(input('Ingrese el numero de compras'))
