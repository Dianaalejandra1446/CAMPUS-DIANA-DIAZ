#Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.

###Variable###
divisibles = []
#Proceso
for num in range(1, 1001):
    if num % 3 == 0: 
        divisibles.append(num)
        print("LOS NUMEROS DIVISIBLES ENTRE TRES SON:")
        print("__"*20)
        print(f"| {num} | Es divisible")    # Agregar el número a la lista
    elif num % 3 != 0:
        print(f"| {num} | No es divisible")

for num2 in range(1, 1001):
    if num2 % 7 == 0:
        divisibles.append(num2) 
        print("LOS NUMEROS DIVISIBLES ENTRE SIETE SON: \n")
        print("__"*20)
        print(f"| {num2} | Es divisible")    # Agregar el número a la lista
    elif num2 % 7 != 0:
        print(f"| {num2} | No es divisible")       # Si el número es divisible por 3 y 7

#Imprimir los numeros
   

  

