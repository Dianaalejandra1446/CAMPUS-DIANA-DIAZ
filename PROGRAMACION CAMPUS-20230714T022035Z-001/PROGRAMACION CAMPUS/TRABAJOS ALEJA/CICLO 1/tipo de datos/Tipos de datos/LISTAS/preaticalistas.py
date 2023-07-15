# Repaso listas

"""numeros = [1, 2, 3, 4, 5,]
print(numeros)
primeraPosicion =numeros[0]

longuitud = len(numeros)
print(f"El primer valor es: {primeraPosicion}\nla longuitud de la lista es: {longuitud}")

for num in numeros:
    print(num)
"""
#Indexado y sublistas

"""lista = ["Dale", "un", "buen", "like", "crack"]
print(lista)
ultimaPosicion = lista[-1]
print(ultimaPosicion)
penultimo = lista[-2]
print(penultimo)

sublista = lista[1:4]#IMPRIME DE 1 HASTA 4
print(sublista)
sublista = lista[:4]#DE 0 A 4
print(sublista)
sublista = lista[:2]#DE 0 A 1
print(sublista)

sublista = lista[-4:-1]
print(sublista)#IMPRIME -4,-3,-2 UN BUEN LIKE"""

#Comprobar si una lista contiene o no un elemento
"""lista = ["Dale", "un", "buen", "like", "crack"]
palabra = "like"
palabraDos = "melocoton"

if palabra in lista:
    print("La palabra pertenece a la lista")

if palabraDos not in lista:
    print("La palabra no esta en la lista")"""

#Modificar elementos en una lista
"""lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print(lenguajes)
lenguajes[1] = "Angular"
print(lenguajes)
lenguajes[0] = lenguajes[0] + "++"
print(lenguajes)

lenguajes[2:4] = ["Anaconda","TypeScript"]
print(lenguajes)

lenguajes[4:5] = ["Varios" , "Valores", "Botella"]
print(lenguajes)"""

#Metodos de las listas,añadir elementos
"""lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]

lenguajes.insert(1, "C++")
print(lenguajes)

lenguajes.append("Typescript")
print(lenguajes)

lenguajesDos = ["Perro", "Helado", "Hamburgesa"]
lenguajes.extend(lenguajesDos)
print(lenguajes)
print(lenguajesDos)

lenguajesDos.extend(lenguajes)
print(lenguajesDos)
"""
#ELIMINAR ELEMENTOS LISTA
frutas =["platano", "kiwi","papaya", "melocoton", "cereza"]
print(frutas)

frutas.pop()#ELIMINAR LA ULTIMA POSICION DE LA LISTA
print(frutas)

elementoEliminado = frutas.pop(0)#ELIMINAR POSICION 0
print(frutas)
print(elementoEliminado)

#OTRA FORMA
frutas.remove("kiwi")
print(frutas)

# ELIMINAR ELEMENTO SIN METODO

del frutas[0]
print(frutas)

indice = frutas.index("melocoton")#INTERCAMBIAR VALOR POR SU POSICION
print(indice)