#SINTAXIS GENERAL,corchete cuadrado es opcional 
"""def nombre_funcion([param1,param2, ..,param3]):
    cuerpo_funcion
"""
#Funcion que sume dos numeros #Devolver respuestas return
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! INgrese un numero valido")

def sumar(num1,num2):
    s = num1 + num2
    return s

a = leerInt("Ingrese un numero: ")
b = leerInt("Ingrese otro numero: ")
print("El resultado de la suma es: ",sumar(a,b))

"""a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))"""
"""print("El resultado de la suma es: ",sumar(a,b))"""

