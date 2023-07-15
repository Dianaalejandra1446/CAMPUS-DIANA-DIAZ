#TENERMOS un texto donde queremos encontrar palabras clave.Las palabras clave pueden ser hasta 5 y debemos pedirselas al usuario y guardarlas en una lista

#Si el usuaruo quiere poner menos de 5 palabras clave,debera escribir "fin" para terminar de introducir datos.Si el usuario introduce numeros o nada,debemos elimarlos de la lista antes de la busqueda,

#En otra lista,debemos guardar el numero de veces que aparece cada palabra clave en nuestro texto.Por ejemeplo si las palabras clave son ordenador y portatul y aparecen 5 y 7 veces respectivamente nuestras listas deben ser asi
#.keywords =["ordenador","portatil"]
#. ocurrencias[5,7]

texto = """Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa.
Es muy importante que logremos tetrabjar efectivamente de manera autorregulada.Esto se traduce en finalizar antes nuestras tareas  y evitar jornadas laborales interminables.
El primer consejo y uno de los mas importantes ya te lo he dado en el apartado anterior
Tenemos que contruir un espacio de trabajo en el que nos sintamis comodos y dispongamos de todas las herramientas necesarias para teletrabajar
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar.
De esta forma ,nuestro cerebro asocia el sitio de accion de trabajar y nos hara estar mas focalizados en nuestras tareas """

keywords = []
ocurrencias = []#NUMERO DE VECES PALABRA CLAVE

for x in range(5):
    keyword = input("Ingrese una palabra o fin para terminar: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)

print(keywords)

posicion = 0
while(True):
    if posicion >=len(keywords):
        break
    if keywords[posicion] == '':
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():#texto = "22" texto.isnumeric() -> True
        keywords.pop(posicion)
    else:
        posicion += 1
print("Lista de keywords corregida")
print(keywords)

texto = texto.split()

for x in range(len(keywords)):
    ocurrencias.append(0)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            ocurrencias[pos] += 1
            break

print(ocurrencias)