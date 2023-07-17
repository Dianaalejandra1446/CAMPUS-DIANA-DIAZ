#Archivos externos

#Modo abrir fichero de lectura

"""fichero = open("CICLO 1\Archivos\demo.txt","rt", encoding='utf-8')
primeralinea = fichero.readline()
print(primeralinea)
print(fichero.readline())
print(fichero.readline())"""


# r ---> read (no modificar solo leer)
# w ---> write (sobreescribir sobre el fichero)
# a ---> append (añade contenido al final del fichero)(añade mas contenido si ya tenermos)
# x ---> create (crea un fichero)

# t --> text mode (ficheros de texto)
# b --> bytes - para archivos como fotos

#Leer con lista 

"""fichero = open("CICLO 1\Archivos\demo.txt","rt", encoding='utf-8')
print(fichero.readline())
todasLasLineas = fichero.readlines()
print(todasLasLineas)

fichero.close()"""

#readlines() convierte las lineas a una lista

#ESCRIBIR FICHERO EXISTENTE
"""fichero = open('CICLO 1\Archivos\demo.txt','w', encoding='utf-8')
fichero.write("Me he cargado todo lo que habia.\n")
listaContenido = [
    'Dimas es el mejor Youtuber.\n'
    'Me turboflipa su',
    'curso de Python.\n',
    'Adios muy buenas.\n'
]
fichero.writelines(listaContenido)
fichero.close()"""

#No escribir el \n

"""fichero = open('CICLO 1\Archivos\demo.txt','w', encoding='utf-8')
fichero.write("Me he cargado todo lo que habia.\n")
listaContenido = [
    'Dimas es el mejor Youtuber',
    'Me turboflipa su curso de Python',
    'Adios muy buenas.'
]
listaContenido = list(map(lambda line: line +'\n',listaContenido))
print(listaContenido)
fichero.writelines(listaContenido)
fichero.close()
"""
#Escribir en un fichero existente modo append añadir contenido sin eliminar el existente
"""fichero = open('CICLO 1\Archivos\demo.txt','a', encoding='utf-8')
fichero.write('\n\n\nEsto es una nueva linea')"""

#Apartado 4:Crear un nuevo fichero

"""try:
    fichero = open('CICLO 1\Archivos\demo2.txt','x', encoding='utf-8')#X ---> CREAR UN FICHERO
    fichero.write("Soy un fichero nuevoo")
    print(fichero.readable())#TRUE O (FALSE) SI PODEMOS LEER
    print(fichero.writable())#(TRUE) O FALSE SI PODEMOS ESCRIBIR
    fichero.close()
except FileExistsError:
    print("No se puede crear algo que ya existe")"""

#CONTROLAR FUNCION en la cual queremos leer seek

"""fichero = open('CICLO 1\Archivos\demo.txt',encoding='utf-8')
fichero.seek(0)#EMPIEZA A LEER DESDE EL DECIMO CARACTER
print("Estamos leyendo desde el decimo caracter: \n")
print(fichero.read())
fichero.close()"""

#APARTADO DE LECTURA Y ESCRITURA SIMULTANEA
"""fichero = open('CICLO 1\Archivos\demo.txt','r+',encoding='utf-8')#r+ para leer y escribir
lineas = fichero.readlines()#leemos todo y se va al final de la linea
print(lineas)

fichero.write('\nEsta linea es nueva')
fichero.close()"""

#EJERCICIO
import time, random

lista = []
for x in range(50000):
    lista.append(random.randint(0,150000))

fichero = open('CICLO 1\Archivos\Times.txt','wt',encoding='utf-8')

for x in range(100):
    ContadorFor = 0
    starTime = time.time()
    for num in lista:
        ContadorFor =+ num
    elapsedTimeFor = time.time() - starTime

    pos = 0
    contadorWhile = 0
    starTime = time.time()

    while pos < len(lista):
        contadorWhile =+ lista[pos]
        pos =+ 1
    elapsedTimeWhile = time.time() - starTime

    fichero.write(f"{elapsedTimeFor};{elapsedTimeWhile}\n")

fichero.close('./times.txt',encoding= 'utf-8')
fichero()

meanFor = 0
meanWhile = 0
samples = 0

for line in fichero.readlines():
    line.replace('\n', "")
    timeFor, timeWhile = line.split(";")
    meanFor += float(timeFor)
    meanWhile += float(timeWhile)
    samples += 1

print(f"Tiempo for: {(meanFor/samples)*(10**3)} ms. Time While: {(meanWhile/samples)*(10**3)} ms.")
fichero.close()