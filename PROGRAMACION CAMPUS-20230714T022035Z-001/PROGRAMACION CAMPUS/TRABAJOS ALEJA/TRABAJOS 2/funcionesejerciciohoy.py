""" Resuelva los siguientes enunciados en Python haciendo un menú que el usuario pueda ingresar una opción
y lo lleve a la resolución del ejercicio. Por ejemplo:

MENU
1- Cantidad de palabras en un String
2- Calcular el mcd de dos números
3- Calcular el IVA de una factura
4- Salir
>> Escoja una opción (1-4)?

1. Cree una función que retorne el número de palabras presentes en un String que le llega cómo parámetro.
(obs: considere que toda palabra válida está separada por un espacio de la anterior)

2. Diseñar un algoritmo que calcule el máximo común divisor de dos números mediante el algoritmo de
Euclides.

Sean los dos números A y B. El método para hallar el máximo común divisor (mcd) de dos números A
y B por el método de Euclides es:
I. Dividir el número mayor (A) por el menor (B). Si el resto de la división es cero, el número B
es el máximo común divisor.

II. Si la división no es exacta, se divide el número menor (B) por el resto de la división anterior.

III. Se siguen los pasos anteriores hasta obtener un resto cero. El último divisor es el mcd buscado.

3. Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función
sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
#MENU 
def menu():
        print("\n--------------")
        print(" MENU ")
        print("----------------\n")
        print("1.Cantidad de palabras de un string")
        print("2.Calculcar el mcd de dos numeros")
        print("3.Calcular el iva de una factura")
        print("4.Salir")
        print(">> Escoja una opcion (1-4)?")

def cantidadstring ():
    print("\n"* 1, "********* 1.Cantidad de palabras de un string *********")
    palabra = input("\nIngrese una palabra: ")
    total_caracteres = len(palabra)
    if len(palabra) < 1:
        print("Escribe una palabra mas larga: ")
    input("--> Presione cualquier tecla para volver al menu")

def mcdnumeros ():
    print("\n"* 1, "********* 2.Calculcar el mcd de dos numeros *********")
    a = int (input("Ingrese un numero: "))
    b = int (input("Ingrese otro numero: "))
    if a % b = 0:
    print("El maximo comun divisor es", a / b)
    mayor = a
    menor = b
    
def iva ():
    pass

#programa general
    while True:
        if opcion == 1:
            cantidadstring()
        elif opcion == 2:
            mcdnumeros()
        elif opcion == 3:
            iva()
        elif opcion == 4:
            print("\n -----Gracias por usar la MiniCalculadora <3-----")
            break
        else:
            msgError("Opcion invalida")