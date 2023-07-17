import math
ladoa = int(input("Ingrese primer el valor de a: "))
ladob = int(input("Ingrese el el valor de b: "))
ladoc = int(input("Ingresar el el valor de c: "))
ladop = int(input("Ingresar el el valor de d: "))
#formula
if ladop>ladoa and ladop>ladob and ladop>ladoc:
    area = math.sqrt (ladop*(ladop-ladoa)*(ladop-ladob)*(ladop-ladoc))
    print(f"Para un triangulo de lados {ladop},{ladoa},{ladoc},{ladob}")
else:
    print("datos no validos")