#Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.

"""###Variable###
#Imprimir los numeros"""
for num in range(1, 1001):
    if num % 3 == 0 and num % 7 == 0:
        print("LOS NUMEROS DIVISIBLES ENTRE TRES Y SIETE SON:")
        print("__"*20)
        print(f"| {num} | Es divisible") 


  

