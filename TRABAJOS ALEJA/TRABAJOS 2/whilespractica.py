#Escriba un programa que permita generar la tabla de multiplicar de un numero entero postivo N,comenzando desde 1.
#Si el usuario escribe un numero incorrecto(numero negativo o cero ),no se va ejecutar la tabla y se preguntara de nuevo hasta que sea un numero postivo

#Validacion de errores
"""while True:
    try:
        n = int(input("Ingrese un numero entero positivo: "))
        if n > 0:
            print("Es correcto")
        if n < 0 or n == 0:
            print("Numero incorrecto intentelo de nuevo")
            continue
        break
    except ValueError:
        print("Ingrese numeros solamente")

for i in range(1,n + 1):
    print(n, "por", i, "es igual a", n*i)"""

""" Escribe un programa que, al recibir como dato un numero entero postivo N,calcule el resultado de la siguiente serie:
1 +(1/2) + (1/3) + (1/4) + .... + (1/N)

Si el usuario escribe un numero incorrecto,el programa no se ejecuta.En cambio pregunta de nuevo la informacion hasta que el dato sea correcto
"""
while True:
    try:
        n = int(input("Ingrese un numero entero positivo: "))
        if n > 0:

            resultado = 0
            for i in range(1,n+1):

                resultado += (1/i)

            print("El resultado de la serie es:",resultado)
        else:
            print("Numero incorrecto")
            continue
        break
    except ValueError:
        print("Ingresa solo numeros enteros postivos")

