"""Se tiene una la informacion sobre 1 estudiante de una institucion de educacion para el trabajo,que realizara el proceso de matricula financiera.La informacion que se conoce del estudiante es la siguiente
-codigo
-nombre
-Programa academico que pertence
*Tecnico en sistemas == 800.000
*Tecnico desarrollo de videjuegos == 1.000.000
*Tecnico en animacion digital = 1.200.000

IndicadordeBeca,puedeser:
1.Becaporrendimientoacadémico.
Descuentodel 50%  sobreelvalormatricula
2.BecaCultural–Deportes.Descuentodel40%sobreelvalormatrículao3:SinBeca.
3.Sin beca
"""
#MENU ELEGIR PROGRANA
def menu():
        print("\n--------------")
        print(" MENU ")
        print("----------------\n")
        print("1.Tenico en sistemas")
        print("2.Tecnico desarrollo de videjuegos")
        print("3.Tecnico en animacion digital")
        print("4.Salir")
        print(">> Escoja una opcion (1-4)?")

#PROGRAMA GENERAL
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")

def leerString(msg):
    while True:
        try:
            n = input(msg)
            if n.strip() == "":
                print("Error! Ingrese el nombre valido.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError as e:
            print("Error! Hay que ingresar el nombre.")


def leerProgramaAcademico():
    seleccionar = int(input("Elige un programa:"))
    if seleccionar == 1:
        print("Elegiste tecnico en sistemas ")
    elif seleccionar == 2:
        print("Elegiste tecnico desarrollo de videojuegos ")
    else:
        print("Elegiste tecnico en animacion digital")
    return seleccionar

def valorMatricula(ValNetoPagar):
    print("A continuacion se mostrara el costo de programa sin beca incluida")
    if ValNetoPagar == 1:
        print("Su matricula para el programa Tenico en sistemas sin beca es de 800.000")
    elif ValNetoPagar == 2:
        print(f"Su matricula para el programa Tecnico desarrollo de videjuegos sin beca es 1.000.000 ")
    elif valNetoPagar == 3:
        print(f"Su matricula para el programa Tecnico en Animacion digital sin beca es 1.200.000 ")

def leerIndBeca():
    seleccionar = int(input("Elige una beca:"))
    if seleccionar == 1:
        seleccionar = 0.5
        print("Elegiste beca rendimiento academico por 50% ")
    elif seleccionar == 2:
        print("Elegiste beca Cultural del 40%")
        seleccionar = 0.4
    else:
        print("No selecciono ninguna beca")
        seleccionar = 0
    return seleccionar
    
def calMatricula(progAcad,beca):
    valor = 0
    if progAcad == 1:
        valor = 800000
    elif progAcad == 2:
        valor = 1000000
    elif progAcad == 3:
        valor = 1200000
    total = valor -(valor*beca)
    return total


cod = leerInt("Ingrese el codigo del estudiante: ")
nom = leerString("Ingrese el nombre deñ estudiante")
progAcad = leerProgramaAcademico()
beca =leerIndBeca()

valNetoPagar = calMatricula(progAcad,beca)

print("\n", "-"* 40)
print("Estudiante: ",nom)
print(f"El valor neto a pagar es: {valNetoPagar:.0f}")
