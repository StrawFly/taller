from productos import Pan, Pastel

# Lista global en memoria
inventario = []

def agregar_producto(tipo, nombre, precio, caracteristica):
    if tipo == "pan":
        producto = Pan(nombre, precio, caracteristica)
    elif tipo == "pastel":
        producto = Pastel(nombre, precio, caracteristica)
    inventario.append(producto)
    print(f"✅ {producto.nombre} añadido al inventario.")

def mostrar_inventario():
    print("\n--- INVENTARIO DE PANADERÍA ---")
    for producto in inventario:
        print(producto)