"""Dada la siguiente informacion sobre las calificaciones educativa
.Codigo
.Nombre
.Nota 1 (Peso de 30%)
.Nota 2(Peso de 30%)
.Nota 3(Peso de 40%)
El proceso termina cuando el codigo que se ingrese sea 999(Bandera)
Se pide calcular:

La nota definitiva de cada estudiante e indicar con un mensaje si aprobo o reprobo,utilizando funciones
Para aprobar la nota debe ser mayor o igual a 3.0 y la informacion es su totalidad se debe almacenar en diccionarios
"""
def calnotadefi():
    notadef = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4
    
    return notadef

calificaciones = {}

while True:
    codigo = int(input("Ingrese codigo: "))
    if codigo== 999:
        break

    nombre = input("Ingrese el nombre del estudiante:")
    nota1 = float (input("Ingrese su nota 1: "))
    nota2 = float(input("Ingrese su nota 2: "))  
    nota3 = float(input("Ingrese su nota 3"))

    calificaciones[codigo] = {}
    calificaciones[codigo]["nota1"] = nota1
    calificaciones[codigo]["nota2"] = nota2
    calificaciones[codigo]["nota3"] = nota3

    otroest = input("Desea agregar otro estudiante?\n S/ \n N = 999")
    if otroest == "999":
        break
    
print("\n\n *** NOTAS FINALES ***")
print("="*30)
for k in calificaciones.keys():
    n = calnotadefi
    if n >= 3 and n <= 5:
     print(calificaciones[k]["nombre"], f"La calificacion del estudiante es{n} PASASTE LA MATERIA")
    else:
     print(calificaciones[k]["nombre"], f"La calificacion del estudiante es{n} NO PASASTE LA MATERIA")
print("=" * 30)



