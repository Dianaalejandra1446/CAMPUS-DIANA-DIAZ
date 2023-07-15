def adicionar(dicc,clave,valorNuevo):
    dicc[clave]= valorNuevo
    return 

def adicionarCarro(dicc):
    clave= input("Ingrese una placa: ")
    valor= input("Ingrese una marca: ")
    adicionar(dicc,clave,valorNuevo)

def modificar(dicc,clave,valorNuevo):
    dicc[clave]=valorNuevo
    return dicc
def modificarCarro(dicc):
    clave= input("Ingrese una placa: ")
    valor= input("Ingrese una marca: ")
    modificar(dicc,clave,valor)
def borrar(dicc,clave):
    del dicc[clave]
    return dicc
def BorrarCarro(dicc):
    clave=input("Ingrese una placa")
    borrar(dicc,clave)
def buscar(dicc,clave):
    return clave in dicc
def bucarCarro(dicc):
    clave = input("Ingrese la placa a buscar")
    if(buscar(dicc,clave)):
        print("La placa se encuentra en el diccionario")
        print(dicc)
    else:
        print("La placa NO esta")
        print(dicc)
op = 6
dicCar = {}
while(op!=6):
    op = int(input("Opciones\n 1.crear\n 2.Modificar \n 3.Borrar \n 4.Listar \n 5.Buscar \n 6.Salir"))
    if (op == 1):
        adicionarCarro(dicCar)
    elif(op == 2):
        modificarCarro(dicCar)
    elif(op == 3):
        modificarCarro(dicCar)
    elif(op == 4):
        print(dicCar)
    elif(op == 5):
        buscarCarro(dicCar)
