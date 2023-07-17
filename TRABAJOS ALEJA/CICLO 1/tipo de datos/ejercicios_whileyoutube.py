#Cree un ciclo for que imprima los valores de 7 a 14
"""for valores in range(7,15):
    print(f"El valor del bucle es {valores}")"""
#Cree el ciclo con while
"""valores = 7

while valores <= 14:
    print(f"El valor del bucle es {valores}")
    valores += 1"""
#Crear un bucle for y luego un while que muestre el valor del bucle es: con valores del 0 al -5000 en decrementos de 500

"""
for valor in range(0,500,-5001):
    print (f"el valor del bucle es: {valor}")"""

"""#Construya un programa que verifique si un número dado es perfecto. Un número perfecto es un
número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo el
número mismo). En otras palabras, si sumas todos los divisores propios de un número perfecto, el
resultado será igual al número original.
Por ejemplo, el número 6 es considerado un número perfecto. Sus divisores propios son 1, 2 y 3. Si
sumamos estos números: 1 + 2 + 3 = 6, obtenemos el mismo número original."""

"""numero = int(input("Ingrese un numero: "))
contador = 1
suma = 0

while contador < numero:
    if numero % contador == 0:
        suma += contador
    contador += 1

if suma == numero:
    print(f"El numero {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")
"""
#De una serie de números ingresados por el usuario, imprima cuales de estos son primos y cuáles no.El ingreso de los números se termina cuando el usuario ingrese un numero negativo.

numeros = 0
numero= int(input("Ingrese un numero"))
while numero >= 0:
    if numero < 0:
        break
    numeros = 0
    for i in range(1,numero)
    if numero % numero == 0 and numero % 1 == 0:
        print(f"El numero {numero} es primo")
        numeros == 0
    else:
        print(f"El nuemro {numero} no es primo")

