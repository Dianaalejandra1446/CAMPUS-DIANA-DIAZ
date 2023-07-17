#Estructura de control while
"""
numero = 1

while numero <= 10:
    print(numero)
    numero += 1 
prin("Fin")"""

"""Mostrar la suma de los numeros multipos de 5 menores a 50
5+10+15.. + 45
"""
"""#Sumar multiplos de 5
numeromax = int(input("Introduce el numero maximo:"))
contador = 0
suma = 0

while contador < numeromax:
    suma = suma + contador
    contador += 5
print("La suma es: ",suma)"""
"""
#TABLA MULTIPLICAR NUMERO 7
#SOLICITAR
tabla = int(input("Introduce la tabla de multiplicar: "))
inicio = 1

while inicio <= 10:
    resultado = tabla * inicio
    print(tabla,"*",inicio,"=",resultado)
    inicio += 1"""

"""#Mostrar la suma y cantidad de numeros pares comprendidos entre dos numeros ingresados por el teclado

numeroinicial = int(input("Ingrese un numero incial: "))
numerofinal = int(input("Ingrese un numero final: "))
cantidadpares = 0

while numeroinicial < numerofinal:
    if numeroinicial% 2 == 0:
        print(numeroinicial)
        cantidadpares += 1
    numeroinicial += 1

print("hay",cantidadpares,"numeros pares")"""

"""#EJEMPLO FOR
for i in range(3,12,3):
    print(f"E valor del bucle es: {i}")"""

"""
colores = ["rojo","azul","verde","amarillo"]

print("---Listado de colores---")

for color in colores:
    if color == "azul":
        print(f"Se ha roto la ejecucion del bucle")
        break  
    print(f"-Color {color}-")
"""
"""

    i = 1

while i >= -5:
    print(f"El valor del bucle es: {i}.")
    i -= 1"""
while True:
    salida = input("Introduce 'salir' para finalizar.\n").lower()
    if salida == 'salir':
        break