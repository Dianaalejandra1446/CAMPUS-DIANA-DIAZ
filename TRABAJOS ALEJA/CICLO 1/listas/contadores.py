#Introducir 5 número y contar los números pares.

#

#Introducir 5 número y sumar los números pares.

suma = 0
for var in range(1,6):
	num = int(input("Dime un número:"))
	if num % 2 == 0:
		suma = suma + num
print("La suma de los números pares es ",suma)
