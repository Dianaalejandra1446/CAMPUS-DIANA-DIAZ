#ejercicio 1
nombre= str (input("Ingrese su nombre estudiante "))
reto1 = int (input("Ingrese su nota del reto 1 "))
reto2 = int (input("Ingrese su nota del reto 2 "))
reto3 = int  (input("Ingrese su  del reto 3 "))
ingles= int  (input("Ingrese su nota de ingles "))

print(reto1)
print(reto2)
print(reto3)
print(ingles)
print(nombre)

Notareto1 = reto1 * 0.20
Notareto2 = reto2 * 0.25
Notareto3 = reto3 * 0.35
Notaingles = ingles * 0.20

Notafinal = Notareto1 + Notareto2 + Notareto3 +Notaingles

Notafinal
print(f'La nota final de {nombre} es {Notafinal}')


