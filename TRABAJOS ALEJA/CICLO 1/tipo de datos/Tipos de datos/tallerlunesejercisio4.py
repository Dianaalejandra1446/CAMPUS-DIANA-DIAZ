###Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor y el menor de todos estos números.
num1 = int (input("Ingrese un numero "))
mayor = num1
menor = num1

for repeticion in range(9):
    numero = int(input("Ingrese un número: "))
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
print("El número mayor es:", mayor)
print("El número menor es:", menor)