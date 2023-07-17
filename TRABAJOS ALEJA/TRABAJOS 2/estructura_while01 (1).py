"""Adivina el número: Crea un programa en el que la computadora "piense" un número secreto entre 1 y
100, y el usuario tenga que adivinarlo. El programa debe proporcionar pistas como "Demasiado bajo"
o "Demasiado alto" hasta que el usuario adivine correctamente.
El usuario que gana es el que adivine en el menor número de intentos.

Este programa se hizo en clase. Para el software review modifícalo para que el usuario tenga un limite
de 3 a 5 intentos (escoja un número al azar entre [3, 5]. Cada usuario puede tener un número de intentos
distinto) para adivinar el número.
"""
#Importar un numero random
import random
cantidaduser = int(input("Ingrese la cantidad de usuarios: "))
n = random.randrange(1,101)

for ingresados in range (1,cantidaduser +1):
    nomusuario = input("Ingrese su nombre ")
    numerousuario = int(input("Ingrese un numero: "))

for limite in range (1,6):
    if ingresados > 5:
        print("Perdiste,Lo siento acabaste tus intentos")
        
totalintentos =ingresados
nmayor = totalintentos
nmenor = totalintentos


#Verificar si hay un error
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

#Ingrese mas numero o gano o perdio    
while True:
    if numerousuario != n:
        print(f"El usuario {nomusuario} ingreso el numero equivocado ingrese otro")
        numerousuario = int(input("Ingrese un numero: "))
    if numerousuario == n:
        print("Felicitaciones acertaste")
    elif numerousuario == nmayor:
        print(f"El usuario {nomusuario} perdio ya que tuvo mayor intentos")
    elif numerousuario == nmenor:
        print(f"El usuario {nomusuario} perdio ya que tuvo menor intentos")