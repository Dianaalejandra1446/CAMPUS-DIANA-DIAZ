def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! INgrese un numero valido")

def msgError(msg):
    print("----> !ERROR ",msg)
    input("-----> Presione cualquier tecla para continuar")
def menu():
    while True:
        print("\n**************")
        print(" MENU ")
        print("**************\n")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Potencia")
        print("6.Factorial")
        print("7.Salir")
        op = leerInt("\n>> Opcion (1 a 7)? ")
        if op < 1 or op > 7:
            msgError("Opcion no valida")
            continue
        return op
        

def sumar():
    print("\n"* 3, "*** 1.SUMAR ***")
    n1 = leerInt("Ingrese un numero: ")
    n2 = leerInt("Ingrese otro numero: ")
    print("\n ==> El resultado de la suma es: ", n1 +n2)
    input("--> Presione cualquier tecla para volver al menu")

def restar():
    print("\n"* 3, "*** 1.RESTAR ***")
    n1 = leerInt("Ingrese un numero: ")
    n2 = leerInt("Ingrese otro numero: ")
    print("\n ==> El resultado de la suma es: ", n1 - n2)
    input("--> Presione cualquier tecla para volver al menu")

def multiplicar():
    print("\n"* 3, "*** 1.MULTIPLICAR ***")
    n1 = leerInt("Ingrese un numero: ")
    n2 = leerInt("Ingrese otro numero: ")
    print("\n ==> El resultado de la suma es: ", n1 * n2)
    input("--> Presione cualquier tecla para volver al menu")

def dividir():
    while True:
        print("\n"* 3, "*** 1.DIVIDIR***")
        n1 = leerInt("Ingrese un numero: ")
        n2 = leerInt("Ingrese otro numero: ")  

        if n1== 0 or n2 == 0:
            print("El numero no se puede dividir")
        else:
            print("\n ==> El resultado de la division es: ", n1 / n2)
            input("--> Presione cualquier tecla para volver al menu") 
            break
        
            
        
def potencia():
    print("\n"* 3, "*** 1.POTENCIA ***")
    n1 = leerInt("Ingrese un numero: ")
    n2 = leerInt("Ingrese el numero para elevar la potencia: ")
    print("\n ==> El resultado de la suma es: ", n1 ** n2)
    input("--> Presione cualquier tecla para volver al menu")

def factorial():
    print("\n"* 3, "*** 6.FACTORIAL ***")
    n1 = leerInt("Ingrese un numero: ")
    f = 1
    for i in range(1,n1 +1):
        f *= i
    print("\n ==> El resultado de la suma es: ",f)
    input("--> Presione cualquier tecla para volver al menu...")


#PROGRAMA GENERAL
while True:
    opcion = menu()

    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion==3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        potencia()
    elif opcion == 6:
        factorial()
    elif opcion == 7:
        print("\n -----Gracias por usar la MiniCalculadora <3-----")
        break
    else:
        msgError("Opcion invalida")