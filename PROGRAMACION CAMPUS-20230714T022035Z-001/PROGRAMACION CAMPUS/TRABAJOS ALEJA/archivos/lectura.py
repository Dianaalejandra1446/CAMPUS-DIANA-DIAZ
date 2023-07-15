import io

#Abrirlo
fd =open("archivos/texto.txt","r", encoding="utf-8")
fd.seek(55)#caracteres
leer2 = fd.readline(6)
leer3 = fd.readlines()
"""leer = fd.read()"""
#leer2 = fd.readline()#lee el cambio de linea
#leer3 = fd.readlines()
fd.close()
print(leer2.rstrip())
print(leer3)

"""print(leer3[1].rstrip(), end="*")"""#RSTRIP CARACTERES A LA DERECHA #Corchetes imprime la linea