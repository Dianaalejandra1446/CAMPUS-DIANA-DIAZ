ruta = "CICLO 1\Archivos\miarchivo.txt"
fd = open(ruta,"w")
"""fd = open(ruta,"r+")"""#leer y escribir desde el principio

fd.write("Refuerzo archivos")
fd.close(fd)
print("Fin del programa")

ruta = "CICLO 1\Archivos\miarchivo.txt"
fd = open(ruta,"a+")#a+ agregar y leer
fd.write("\nSabado de esfuerzo archivos")
fd.seek(0)#que linea empieza
lectura = fd.readline()
fd.close(fd)
print("Fin del programa")

ruta = "CICLO 1\Archivos\miarchivo2.txt"
fd = open(ruta,"w")
fd.write("\nInicio de copia")
fd.writelines(lectura)
fd.close()