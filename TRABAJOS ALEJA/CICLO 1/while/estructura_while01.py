"""Adivina el número: Crea un programa en el que la computadora "piense" un número secreto entre 1 y
100, y el usuario tenga que adivinarlo. El programa debe proporcionar pistas como "Demasiado bajo"
o "Demasiado alto" hasta que el usuario adivine correctamente.
El usuario que gana es el que adivine en el menor número de intentos.

Este programa se hizo en clase. Para el software review modifícalo para que el usuario tenga un limite
de 3 a 5 intentos (escoja un número al azar entre [3, 5]. Cada usuario puede tener un número de intentos
distinto) para adivinar el número.
"""
import random

cantidaduser = int(input("Ingrese la cantidad de usuarios: "))

n = random.randrange(1,101)

for i in range(cantidaduser):
    nomusuario = input("Ingrese su nombre: ")
    totalintentos = random.randint(3, 5)
    
    for j in range(totalintentos):
        numerousuario = int(input("Ingrese un número: "))

        if numerousuario > n:
            print("Demasiado alto")
        elif numerousuario < n:
            print("Demasiado bajo")
        else:
            print(f"Felicitaciones {nomusuario}, has adivinado el número en {j+1} intentos")
            break
    else:
        print(f"{nomusuario}, has agotado tus {totalintentos} intentos. El número era {n}")

    while True:
        try:
            break
        except ValueError:
            if numerousuario != n:
                print("Ingresa un numero valido!")

            if numerousuario < 1:
                print("Numero demasiado bajo: ")
            if numerousuario > 100:
                print("Numero demasiado alto") 

    while True:
        if numerousuario != n:
            print(f"El usuario {nomusuario} ingreso el numero equivocado ingrese otro")
        numerousuario = int(input("Ingrese un numero: "))

        if numerousuario == n:
            print("Felicitaciones acertaste")
        elif numerousuario == nmayor:
            nmayor = totalintentos
            nmenor = totalintentos
            print(f"El usuario {nomusuario} perdio ya que tuvo mayor intentos")
        elif numerousuario == nmenor:
            nmayor = totalintentos
            nmenor = totalintentos
            print(f"El usuario {nomusuario} perdio ya que tuvo menor intentos")