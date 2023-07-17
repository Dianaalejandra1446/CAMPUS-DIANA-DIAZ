import json

def load_data():
    try:
        with open('datos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def save_data(datas):
    with open('datos.json', 'w') as archive:
        json.dump(datas, archive, indent=4)

def show_data():
    data = load_data()
    if data:
        for elemento in data:
            print(f"id: {elemento['id']}")
            print(f"Título: {elemento['titulo']}")
            print(f"Contenido: {elemento['contenido']}")
            print()
    else:
        print("No hay elementos.")

def find_data(id):
    data = load_data()
    for element in data:
        if element['id'] == id:
            return element
    return None

def create_data(id,titulo, contenido):
    data = load_data()
    element = {
        'id': id,
        'titulo': titulo,
        'contenido': contenido
    }
    data.append(element)
    save_data(data)
    print("Elemento agregado exitosamente.")

def put_data(id, titulo, contenido):
    data = load_data()
    for element in data:
        if element['id'] == id:
            element['titulo'] = titulo
            element['contenido'] = contenido
            save_data(data)
            print("Elemento actualizado.")
            return True
    return False

def delete_data(id):
    data = load_data()
    for index, element in enumerate(data):
        if element['id'] == id:
            data.pop(index)
            save_data(data)
            print("Elemento eliminado exitosamente.")
            return True
    return False

def menu():
    while True:
        print("=== MENÚ ===")
        print("1. Mostrar elementos")
        print("2. Buscar elemento por ID")
        print("3. Agregar elemento")
        print("4. Actualizar elemento")
        print("5. Eliminar elemento")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            show_data()
        elif opcion == "2":
            id = int(input("Ingrese el ID del elemento a buscar: "))
            elemento = find_data(id)
            if elemento:
                print(f"ID: {elemento['id']}")
                print(f"Título: {elemento['titulo']}")
                print(f"Contenido: {elemento['contenido']}")
                print()
            else:
                print("El elemento no fue encontrado.")
        elif opcion == "3":
            id = int(input("Ingrese el ID: "))
            titulo = input("Ingrese el títuloo: ")
            contenido = input("Ingrese el contenido: ")
            create_data(id,titulo, contenido)
        elif opcion == "4":
            id = int(input("Ingrese el ID del elemento a actualizar: "))
            titulo = input("Ingrese el nuevo título: ")
            contenido = input("Ingrese el nuevo contenido: ")
            if not put_data(id,titulo, contenido):
                print("El elemento no fue encontrado.")
        elif opcion == "5":
            id = int(input("Ingrese el ID: "))
            if not delete_data(id):
                print("El elemento no fue encontrado.")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
menu()