#DOS METODOLOGIAS
#.format()
#f-strings

#METODOLOGIA .format 'Cadena aqui {}' .format('algo')

mi_nombre = "Diana"
print('Hola mi nombre es ' + mi_nombre)

print('Esta es una cadena {}'.format('INSERTAR'))

print('El {c} {a} {b}'.format(a='MUY', b='VELOZ',c='CONEJO'))

#FORMATEO DE VARIANTES FLOTANTES "{VALOR:ESPACIO.PRESICIONf}"

resultado= 100/777
resultado
print('El resultado fue de {r:1.4f}'.format(r=resultado))

#CADENAS F-strings

nombre = 'Diana'
print(f'hola mi nombre es {nombre}')

n = 'Alejandra'
e = '24'
print(f'Mi nombres es {n} y mi edad es {e}')

micadena = "Esta es una cadena"
miotracadena = ' Esta tambien es una cadena "disque cadena" '
print(micadena)
print(miotracadena)
print(micadena*3)

#Salto de linea 
cadena = "Esta es una cadena\nHago parte de la misma cadena pero con un salto de linea"
print(cadena)

#tabulacion
cadenatab = "\tEste texto esta esta tabulado"
print(cadenatab)

#IMPRIMIR CARACTERES ESPECIALES
print("salto de \n linea ")
print("tabulacion \t horizontal")
print("contra \\ barra")
print("comilla \' simple ")
print("comilla \" doble")


#Concatenar cadenas caracteres
cadenaconcat1 = "Hola me llamo "
cadenaconcat2 = "Diana"
cadenaconcat3 = cadenaconcat1+cadenaconcat2

print(cadenaconcat3)

print(cadenaconcat1+cadenaconcat2+"=> es esquivalente a => "+ cadenaconcat3)

#TODOEN UNA MISMA IMPRESION
print("Reunimos todo en una misma impresion "+cadena+'\n'+'\t'+cadenatab)