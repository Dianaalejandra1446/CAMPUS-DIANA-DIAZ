#Contruye un programa que al recibir como dato el salario de un profesor de una universidad calcule
#el incremento del salario de acuerdo con el siguente criterio y escriba un nuevo salario del profesor

salario = int(input("Ingrese su salario: "))
if salario < 18000:
    incremento = salario * 0.12
    print(f"Su nuevo salario es:{incremento:.2f}")
elif salario >=18000 and salario <= 30000:
    incremento = salario * 0.08
    print(f"Su nuevo salario es:{incremento:.2f}")
elif salario > 30000  and salario <= 50000:
    incremento = salario * 0.07
    print(f"Su nuevo salario es:{incremento:.2f}")
elif salario > 50000 :
  incremento = salario * 0.07
  print(f"Su nuevo salario es:{incremento:.2f}")

#Construye un programa que determine al recibir como datos dos numeros enteros,si un numero es divisor de otro
n1 = int(input("Ingrese un numero entero: \n"))
n2 = int(input("Ingrese un numero entero: \n"))
resultado1 = int(n1 / n2 )
resultado2 = int(n2 / n1)
if resultado1 % 0 :
    print(f"El numero {n1} es divisible con el {n2}")
elif resultado2 % 0:
    print(f"El numero {n2} es divisible con el {n1}")
else:
    print("El numero no es divisible")