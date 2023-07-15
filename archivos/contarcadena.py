import io

fd = open("archivos/mbox-short.txt", "r", encoding="utf-8")
cont = 0
for linea in fd:
    if linea.count("Subject"): #Empieza con starwitch
        cont += 1

fd.close()
print(f"Cantidad de lineas que empiezan con Subject: {cont} ", )