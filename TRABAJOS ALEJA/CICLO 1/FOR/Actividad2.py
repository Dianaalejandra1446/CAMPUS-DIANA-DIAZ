#Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado de la siguiente serie:
entero = int(input("Ingrese un numero entero: "))
numacumulado = 0
signo = "-"
for num in range (1,entero+1):
    variable = 1/num
    print(f"1/{num} {signo}" , end=" ")
    #SI ES IMPAR SIGNO POSITIVO
    if num % 2 != 0:
        numacumulado = numacumulado + variable 
        signo  = "+"
    #SI ES PAR NEGATIVO
    elif num % 2 == 0:
        numacumulado = numacumulado - variable
        signo = "-"
print("\n El resultado de la operacion anterior es: ", numacumulado)
