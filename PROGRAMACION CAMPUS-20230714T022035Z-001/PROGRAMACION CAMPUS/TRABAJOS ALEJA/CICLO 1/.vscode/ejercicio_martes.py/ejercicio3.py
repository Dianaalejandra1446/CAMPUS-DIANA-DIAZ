"""Contador de vocales: Crea un programa que solicite al usuario ingresar una frase y cuente la cantidad
total de vocales en ella. Utiliza un ciclo "while" para recorrer cada letra de la frase. Si una vocal es
encontrada, incrementa el contador de vocales. Sin embargo, si el usuario ingresa la letra 'q', el programa
debe terminar y mostrar la cantidad total de vocales encontradas hasta ese momento.
"""
contador = 0
numero = 0
frase = input("Ingresa una frase:\n ")

while numero < len(frase):
    letra = frase[numero].lower()
    if letra == 'q':
        break
    elif letra in "aeiou":
        contador += 1
    numero += 1

print(f"La cantidad total de vocales es {contador}")
        