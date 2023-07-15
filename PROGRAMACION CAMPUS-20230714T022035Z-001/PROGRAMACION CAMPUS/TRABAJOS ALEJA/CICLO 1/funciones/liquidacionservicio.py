"""Se tiene una la informacion sobre 1 estudiante de una institucion de educacion para el trabajo,que realizara el proceso de matricula financiera.La informacion que se conoce del estudiante es la siguiente
-codigo
-nombre
-Programa academico que pertence
*Tecnico en sistemas == 800.000
*Tecnico desarrollo de videjuegos == 1.000.000
*Tecnico en animacion digital = 1.200.000

IndicadordeBeca,puedeser:
1.Becaporrendimientoacadémico.Descuentodel50%sobreelvalormatricula
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
            print("Error! Hay que ingresar el nombre.",e.message())


def leerProgramaAcademico(seleccionar):
    seleccionar = int(input("Elige un programa:"))
    if seleccionar == 1:
        print("Elegiste tecnico en sistemas ")
    elif seleccionar == 2:
        print("Elegiste tecnico desarrollo de videojuegos ")
    else:
        print("Elegiste tecnico en animacion digital")

def sistemas():
    pass

def videojuegos():
    pass

def animacion():
    pass

def beca():
    pass
        

cod = leerInt("Ingrese el codigo del estudiante: ")
nom = leerString("Ingrese el nombre deñ estudiante")
progAcad = leerProgramaAcademico()
beca =leerIndBeca()

valNetoPagar = calMatricula(progAcad,beca)

print("\n", "-"* 40)
print("Estudiante: "nom)
print(f"El valor neto a pagar es: f{valorNetoPagar,.0f}")

#ELEGIR MENU
while True:
    opcion = menu()

    if opcion == 1:
        sistemas()
    elif opcion == 2:
        videojuegos()
    elif opcion == 3:
        animacion()
    elif opcion == 4:
        print("\n -----Gracias por elegirnos como estudio <3----")
        break