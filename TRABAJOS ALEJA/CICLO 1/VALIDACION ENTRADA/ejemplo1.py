"""
Dado el nombre y el salario de un empleado, calcular el subisidio de transporte, 
teniendo en cuenta que si el salario es menos o igual a 1200.000 entonces tiene 
derecho a un subsidio de transporte por valor de 120.000 de lo contrario no tiene 
derecho al subsidio de transporte. se debe visualizar el nombre, salario y subsidio 
de transporte."""

nom = input("Ingrese el nombre: ")
sal = int(input("Ingrese el salario: "))

subtrans = 0
if sal <= 1_200_000:
    subtrans = 120_000
else:
    subtrans = 0

print("\n","-")
print("Nombre:",nom)|
print("Salario:",sal)
print("Subsicio",subtrans)
print("-" * 30,"\n")

"""Dado el nombre del estudiante y la calificacion cuantitaiva de una evaluacion (0-100),se pide hallar la calificacion cualitativa

Rango Evaluacion  
0-59                   
60-79                   
80-89                   
90-10  

Evaluacion cualitativa
 D
C
B
A                 

Se pide visualizar,nombre,calificacion cuantitaiva y cualitativa"""

nombre= (input("Ingresa tu nombre "))
calcuanti= int(input("Ingresa tu calificacion "))
if calcuanti >= 0 and calcuanti <= 59:
    calcuali = "D"
elif calcuanti >= 60 and calcuanti <= 79:
    calcuali = "C"
elif calcuanti >= 80 and calcuanti <= 89:
    calcuali = "B"
else calcuanti >= 90 and calcuanti <= 100:

