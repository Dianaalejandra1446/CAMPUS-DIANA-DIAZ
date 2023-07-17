"""Dado el nombre y el estrato (1,2,3,4,5) de un usuario de servicio de energia electrica,calcular loq ue pagaria de tarifa basica del servio de energia electrica,que depende del estrato,asi
Estrato 
1............$10.000
2............$15.000
3............$30.000
4............$50.000
5............$65.000
"""
def calTarifaBasica(estrato):
    if estrato == 1:
        return 10_000
    elif estrato == 2:
        return 15_000
    elif estrato == 3:
        return 30_000
    elif estrato == 4:
        return 50_000
    else:
        return 65_000
    

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


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("Error! Estrato invalido(1 a 5).")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")

#Programa general
nombre = leerString("Ingrse el nombre: ")
estrato = leerInt("Ingrese el estrato del usuario: ")

tarifaBas = calTarifaBasica(estrato)

print("\n","-"*30)
print("Nombre del usuario ",nombre)
print(f"Tarifa basica del usuario: ${tarifaBas:,} ")
print("-"*30)