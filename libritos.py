import json
from libro import Libro

ARCHIVO = "datos.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(lista):
    with open(ARCHIVO, "w") as f:
        json.dump(lista, f, indent=2)

def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    paginas = input("Páginas: ")
    
    nuevo_libro = Libro(titulo, autor, paginas)
    libros = cargar_datos()
    libros.append(nuevo_libro.to_dict())
    guardar_datos(libros)
    print(" Libro añadido!")

def mostrar_libros():
    libros = cargar_datos()
    print("\n--- LIBROS ---")
    for libro in libros:
        print(f"{libro['titulo']} ({libro['paginas']} páginas)")

while True:
    print("\n1. Añadir libro\n2. Ver libros\n3. Salir")
    opcion = input("Opción: ")
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        break
    else:
        print(" Opción no válida")