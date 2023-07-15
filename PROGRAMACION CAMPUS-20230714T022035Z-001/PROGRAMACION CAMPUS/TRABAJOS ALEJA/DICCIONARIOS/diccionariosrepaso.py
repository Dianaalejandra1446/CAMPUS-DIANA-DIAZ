diccionario = {
        'int': 7,
        'str': 'Hola',
        'bool': True,
        'float': 3.5
       }
dic1 = {10:7,
        20:(1, 2, 3,),
        30: ['Control','Educacion']}

tienda = {'item': ['Lapiz','Carpeta','Marcador'],
        'cantidad': [3, 10, 5],
        'valor': [3.50, 4.25, 7.85]}

datos = {'nombre': 'Segio',
            'edad': 25,
            'Genero': 'M'}

for i, j in datos.items():
    print(f'Su {i} es {j}')

del datos ['edad']
print(datos.values())
print(datos.keys())
print(datos.items())

print(tienda['item'][1])
print(diccionario['bool'])
print(dic1[30][1])


