"""Juego de adivinar un numero-
El sistema a travez de la funcion random,genera un numero al azar entre 8 y 9.
El operador debe lanzar un numero tratando de adivinar el caso.En la medida que realice los intentos y no adivine,se incrementa el contador para el momento de adivinar el numero se le informe al operador cual es el numero que adivino e intento
"""
import random 
import so
numero = random.randint(0,9)
cantidad = 0 
num = ''

#ESTRUCTURA WHILE
while numero!= num:
    so.system()