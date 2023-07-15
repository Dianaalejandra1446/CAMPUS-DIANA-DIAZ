"""archivo = open("CICLO 1\Archivos\datos.txt",encoding="utf-8")
texto = archivo.read(5)#PODEMOS PONER EL NUMERO DE CARACTERES QUE LEA
print(texto)

archivo.close()"""
"""
with open("CICLO 1\Archivos\datos.txt","r",encoding="utf-8") as archivo:
    linea = archivo.readline()#IMPRIME LINEA DE TEXTO
    print(linea)
    lineas = archivo.readlines()#Convierte a una lista cada renglon del archivo
    print(lineas)
with open("CICLO 1\Archivos\personas.txt","a",encoding="utf-8") as archivo:#Con with el close lo hace de una forma explicita,W borra y sobreescribe# a = append
    archivo.write("Raul 22\n")
    archivo.write("Diana 19")
"""

pasajeros = {}
with open("CICLO 1\Archivos\datos_metro.csv", "r", encoding="utf-8") as archivo:
    archivo.readline() #quita encabezado
    estaciones = archivo.readlines()#info relevante
    for estacion in estaciones:
        lista = estacion.strip().split(",")
        pasajeros[lista[0]] = list(map(int,lista[1:]))

print(pasajeros)