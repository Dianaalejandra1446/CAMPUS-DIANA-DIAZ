#Escribe un programa en Python que determine si un año ingresado por el usuario es bisiesto o no. Un año bisiesto es aquel que es divisible entre 4, excepto aquellos divisibles entre 100 pero no entre 400.El programa debe realizar lo siguiente:Solicitar al usuario que ingrese un año.Verificar si el año cumple con las condiciones para ser bisiesto.Mostrar un mensaje indicando si el año es bisiesto o no.

año =int (input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("El año",año," es bisiesto")
else:
    print("El año",año,"no es bisiesto")