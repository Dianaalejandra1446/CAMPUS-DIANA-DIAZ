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
print(ficjero.readline())
todasLasLineas = fichero.readlines()
print(todasLasLineas)

fichero.close()"""

#readlines() convierte las lineas a una lista

#ESCRIBIR FICHERO EXISTENTE
fichero = open('CICLO 1\Archivos\demo.txt','w', encoding='utf-8')