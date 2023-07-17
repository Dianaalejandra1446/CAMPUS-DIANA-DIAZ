#Escriba un programa que reciba un número entero positivo y muestre en pantalla la cantidad de dígitos que este tiene.No puede convertir el número a cadena, ni usar funciones de cadena. Solo operadores aritméticos.

numero = int(input("Ingrese un numero entero positivo "))
contador = 0

if num == 0:
    contador = 1
    numero = numero //10
    contador = contador + 1
    print(f"El numero tiene {contador} digitos")