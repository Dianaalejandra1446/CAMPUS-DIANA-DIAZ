"""Ejemplo q
Hacer un programa que ayude a un profesor con las notas de estudiantes.
El prodesor ingresa la nota de 10 estudiantes que tiene y el programa le muestra el promedio de las notas,la nota mayour,la nota  menor y las primeras notas de mayor a menor"""
def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n > 5:
                print("Error! Ingrese una nota validad (0 a 5).")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese una nota valida valido")

notMen = -1
notMay = 6
sumNotas = 0
promNotas = 0.0
lstNotas = []
for est in range(1,11):
    nota = leerFloat(f"Ingrese nota estudiante #{est}:")
    lstNotas.append(nota)

notaMen = min(lstNotas)
print("La nota menor es: ",notMen)
notMay = max(lstNotas)
print("La nota mayor es: ",notMay)

promNotas = sum(lstNotas) / 10
print("El promedio de las notas es: ", promNotas)

lstNotas.sort(reverse=True)
tresNotas = lstNotas[0:3]
strNotas = ""
for nota in tresNotas:
    strNotas += str(nota) + "," 
print("La tres mejores notas son: ", strNotas)