"""Logotipo de Compay

Una marca multinacional de reciente apertura ha decidido basar su logo de empresa en los tres
caracteres más comunes en el nombre de la empresa. Ahora están probando varios
combinaciones de nombres de empresas y logotipos basados en esta condición. Dada una cadena, que
es el nombre de la empresa en minúsculas, su tarea es encontrar las tres más comunes
caracteres en la cadena.
Imprima los tres caracteres más comunes junto con el número de ocurrencias.
Ordenar en orden descendente de recuento de ocurrencias.
Si el recuento de ocurrencias es el mismo, ordene los caracteres en orden alfabético.
Por ejemplo, según las condiciones descritas anteriormente, GOOGLE tendría su logotipo
con las letras G, O, E.
Formato de entrada
Una sola línea de entrada que contiene la cadena S.
Restricciones
3 < largo(S) < 10^4
S tiene al menos 3 caracteres distintos
Formato de salida
Imprima los tres caracteres más comunes junto con su ocurrencia cuente cada uno en un
línea separada.
Ordene la salida en orden descendente de recuento de ocurrencias.
Si el recuento de ocurrencias es el mismo, ordene los caracteres en orden alfabético.
Entrada de muestra 0

aabbbccde

Salida de muestra 0

segundo 3
un 2
c 2

Explicación 0
aabbccde
Aquí, b ocurre 3 veces. Se imprime primero.
Tanto a como c ocurren 2 veces. Entonces, a se imprime en la segunda línea y c en la tercera línea porque
a viene antes de c en el alfabeto.
Nota: La cadena S tiene al menos 3 caracteres distintos."""

contador = 0
numerocar = 0
cadena = input("Ingrese un nombre para la empresa: ")
caracteres = len(cadena)

print("*"*30)
print("CREAR LOGO MARCA")
while numerocar < len(cadena):
    letra = cadena[numerocar].lower()
    if letra in cadena:
        contador += 1
    numerocar += 1

print("El total de caracteres es : ",contador)

listacar = cadena.split()
FrecuenciaCar = []
for i in listacar:
    FrecuenciaCar.append(listacar.count(i))
print(f"Los caracteres mas repetidos son: {listacar}")

listacar.sort()
print(FrecuenciaCar)