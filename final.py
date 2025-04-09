from datos import agregar_producto, mostrar_inventario

while True:
    print("\n1. Añadir pan\n2. Añadir pastel\n3. Ver inventario\n4. Salir")
    opcion = input("Opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del pan: ")
        precio = float(input("Precio: "))
        tipo_masa = input("Tipo de masa: ")
        agregar_producto("pan", nombre, precio, tipo_masa)
    elif opcion == "2":
        nombre = input("Nombre del pastel: ")
        precio = float(input("Precio: "))
        relleno = input("Relleno: ")
        agregar_producto("pastel", nombre, precio, relleno)
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("¡Hasta luego! ")
        break
    else:
        print(" Opción inválida")