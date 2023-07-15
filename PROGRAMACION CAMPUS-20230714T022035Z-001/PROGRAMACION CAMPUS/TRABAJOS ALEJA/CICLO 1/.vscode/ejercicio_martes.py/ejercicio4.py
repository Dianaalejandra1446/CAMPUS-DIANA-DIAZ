"""Hacer un programa que pida al usuario un texto como contraseña y el programa debe validar si es válida.
Una contraseña es válida si:
• Tiene una longitud mínima de 8 caracteres
• Debe contener una letra en minúscula
• Debe contener una letra en mayúscula
• Debe contener un número
• No puede contener espacios
• Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)
"""
print("Ingrese una contraseña valida ")
contraseña = input("Ingrese su contraseña: ")

if len(contraseña) < 8:
    print("Contraseña muy corta,debe tener mas de 8 caracteres")

else:
    minuscula = False
    for minus in contraseña:
        minuscula = True
    if not minuscula:
        print("La contraseña debe tener al menos una miniscula")
        mayuscula = False
    for mayus in contraseña:
        if mayus.isupper()==True:
            mayuscula = True
        if not mayuscula:
            print("La contraseña debe tener al menos una mayuscula")

num = False
for carac in contraseña:
    if carac.isdigit()== True:
        num = True
    if not num:
        print("La contraseña debe tener al menos un numero")
    if contraseña.count(" ")>0:
        print("La contraseña mo puede contener espacios en blanco")
    else:
        print("Contraseña segura")