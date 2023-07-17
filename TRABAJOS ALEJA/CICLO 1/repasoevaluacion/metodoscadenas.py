#POSICION CARACTER
mail = "correo@gmail.com"
posicion = mail.index("@")#BUSCA SI CONTIENE UN @,si no encuentra devuelve Value Error
print(posicion)

posicion = mail.find("@")#Devuelve -1 si el caracter no existe
print(posicion)

#SPLIT,REPLACE,JOIN
compra = "chocolate, pan, agua, platanos, pipas, verduras"
compra2 = "chocolate, pan, agua, platanos, pipas, verduras"
#saber cuantos elementos
listaCompra = compra.split(', ')#Separar string con el elemento que pongamos en comillas
listaCompra2 = compra.split()
print(listaCompra)
print(listaCompra2)

print(f"En la lista de compra tenemos {len(listaCompra)} elementos")#Contar elementos junto len

compraGuiones = compra.replace(', ','; ')
print(compraGuiones)
compra2 = compra2.replace(', ',' ')#CAMBIAR UN CARACTER ESPECIFICADO
print(compra2)

compra = "/".join(listaCompra)
print(compra)

