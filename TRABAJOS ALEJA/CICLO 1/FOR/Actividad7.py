"""7. Mostrar en pantalla si dos números enteros positivos n1 y n2 son amigos. Los números amigos son pares
de números enteros positivos en los cuales la suma de los divisores propios de cada número es igual al
otro número. En otras palabras, dos números amigos cumplen la condición de que la suma de los
divisores propios de uno de ellos es igual al otro número, y viceversa. Por ejemplo, el par de números
(220, 284) es un par de números amigos. Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 y 110. Si sumamos estos números, obtenemos 284, que es el segundo número del par. Por otro lado,
los divisores propios de 284 son 1, 2, 4, 71 y 142, y si los sumamos, obtenemos 220, que es el primer
número del par."""

num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))

sum1 = 0
sum2 = 0

for i in range (1,num1):    
    if num1 % i == 0:
        sum1 += i       
        

print("\n")
for i in range (1,num2):    
    if num2 % i == 0:
        sum2 += i


if sum1 == num2 and sum2 == num1:
    print(f"\nLos numeros {num1} y {num2} son amigos\n")

else:
    print(f"\nLos numeros {num1} y {num2} no son amigos\n")