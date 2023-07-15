"""Búsqueda de palabra clave: Escribe un programa que solicite al usuario que ingrese una oración y una
palabra clave específica. El programa debe verificar si la palabra clave está presente en la oración y
mostrar un mensaje apropiado. Si la palabra clave se encuentra, el programa debe detenerse y mostrar
un mensaje de éxito. Si la palabra clave no se encuentra en la oración, el programa debe continuar
pidiendo al usuario que ingrese otra oración hasta que se encuentre la palabra clave o el usuario ingrese
"salir" para terminar el programa.
"""
clave = input("Ingrese una clave")

while True:
    oracion = input("Ingrese una oracion o escribe fin para terminar el programa" )
    if oracion.lower() =="fin":
        print("El programa fue finalizado")
        break
    
    clave = input("Ingrese una clave")
    if clave.lower() in oracion.lower():
        print("La palabra clave esta en la oracion :D")
        break
    else:
        print("La palabra clave no esta en la oracion.Intentalo de nuevo")