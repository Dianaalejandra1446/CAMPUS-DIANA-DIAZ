import io

fd = open("archivos/mbox-short.txt", "r", encoding="utf-8")
cont = 0
for linea in fd:
    if linea.lower().find("from") > -1:#Empieza con starwitch
        cont += 1

fd.close()
print(f"Cantidad de lineas que empiezan con From: {cont} ", )