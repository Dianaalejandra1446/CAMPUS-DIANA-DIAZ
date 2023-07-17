#Diseñe y escriba un programa que solicite tres números enteros (pueden ser positivos o negativos) y como salida los muestre en orden de mayor a menor.

numero1 = int (input('Ingrese un numero entero'))
numero2 = int (input('Ingrese un numero entero'))
numero3 = int  (input('Ingrese un numero entero'))

#ORGANIZAR
if numero1 > numero2 and numero2 > numero3:
    print("",numero1,"-",numero2,"-",numero3)
    print(numero1,"mayor que",numero2,"mayor que",numero3,"es menor")
elif numero1 > numero3 and numero3 > numero2:
    print("",numero1,"-",numero3,"-",numero2)
    print(numero1,"mayor que",numero3,"mayor que",numero2,"es menor")
elif numero2 > numero1 and numero1 > numero3:
    print("",numero2,"-",numero1,"-",numero3)
    print(numero2,"mayor que",numero1,"mayor que",numero3,"es menor")
elif numero2 > numero3 and numero3 > numero1:
    print("",numero2,"-",numero3,"-",numero1)
    print(numero2,"mayor que",numero3,"mayor que",numero1,"es menor")
elif numero3 > numero1 and numero1 > numero2:
    print("",numero3,"-",numero1,"-",numero2)
    print(numero3,"mayor que",numero1,"mayor que",numero2,"es menor")
elif numero3 > numero2 and numero2 > numero1:
    print("",numero3,"-",numero2,"-",numero1)
    print(numero3,"mayor que",numero2,"mayor que",numero1,"es menor")
else:
    print("Se ingresaron numeros iguales")