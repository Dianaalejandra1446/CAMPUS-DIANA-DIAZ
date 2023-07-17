#MANEJO EXCEPCIONES
#Corregir errores

"""def division(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print(resultado)
        print("No se puede divir por cero")

division(5,5)
division(5,0)"""

#Gestion tipos exepciones
#EXEPCION NUMERO ENTERO Y POSICION

"""frutas = ["0-Platano","1-Manzana","2-Pomelo","3-Melocoton"]

def elegirFrta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige una fruta (por el numero): "))
        print(f"Tu fruta favorita es {listaFrutas[index]}")
    except IndexError:#Si intentamos acceder a una posicion que no existe
        print(f"Indice incorrecto,debe estar entre 0 y {len(listaFrutas)-1}")
    except ValueError:
            print("Ingresa un numero entero")
"""
#EXEPCION BASE A 

"""frutas = ["0-Platano","1-Manzana","2-Pomelo","3-Melocoton"]

def elegirFruta(listaFrutas):
    try:
        print(listaFrutas)
        index = int(input("Elige una fruta (por el numero): "))
        print(f"Tu fruta favorita es {listaFrutas[index]}")
    except Exception as errorRandom:
        print("Ha ocurrido un error,algo ha salido mal")
elegirFruta(frutas)"""

#Apartado: Else,Finally,Raise

while True:
    try:
        total = 0
        sumandos = input("Ponme numeros separados por espacios: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("El valor no es un numero")
    except ValueError:
        print("Los datos son incorrectos")
        print("Vuelva a introducir los numeros ")
    else:
        print(f"El valor de la suma es {total}")
        break
    finally:
        print("Ha termiando la iteracion")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

"""TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.

ZeroDivisionError : Ocurre cuando se itenta dividir por cero.

OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.

IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.

KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.

FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.

ImportError : Ocurre cuando falla la importación de un módulo."""