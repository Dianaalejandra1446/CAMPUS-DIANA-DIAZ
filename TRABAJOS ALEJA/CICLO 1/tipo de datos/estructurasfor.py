"""for i in range(6):
    print(i,end=", ")"""
"""
for i in range(-1, 5):
    print(i,end=", ")"""
"""
for i in range(-1, 5, 2):
    print(i,end=", \n ")"""

#EJERCICIO 1
"""
for par in range(2,101,2):
    print(par, end=", ")"""

#EJERCICIO 2 hacer un programa que calcila el factorial de un nuevo. factoria 5 = 1*2*3*4*5 = 120
"""
n = int(input("Ingrese el valor de N: "))

fact = 1
for i in range(1,n+1):
    fact = fact * i

print(f"El factorial de {n} es: {fact}")"""
#EJERCICIO 3 Determinar e imprimir si un numero es primo o no

n= int(input("Numero? "))

primo = True
for i in range(2,n):
    if n % i == 0:
        primo = False
        culpable = i
    
if primo:
    print("El numero es primo")
else:
    print("El numero no es primo,lo divide",culpable)