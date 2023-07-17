#Crear un programa para saber si un numero ingresado es par o impar
"""
numero = int(input('Ingrese su numero'))

if numero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')"""

#Crear un programa que pregunte al usuario su edad y se muestre en pantalla 
#Si el usuario tiene entre 14-17 años es adolescente
# Y si el usuario tiene entre 5-13 años es niño
"""
edad = int (input('Ingrese su edad '))

if edad >= 18:
    print('Es mayor de edad')
elif edad >= 14 and edad <= 17:
    print('Es adolescente')
elif edad >= 5 and edad <= 13:
    print('Es un niño')"""

#Crear un programa que guarde una contraseña en una variable
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña que introduce el usuario coincide con la que guarda la variable.

clavePorDefecto = 'prueba123'

claveUsuario = input('Ingrese la contraseña: ')

if clavePorDefecto == claveUsuario:
    print('La contraseña conincide')
else:
    print('la contraseña no coincide')