class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Pan(Producto):
    def __init__(self, nombre, precio, tipo_masa):
        super().__init__(nombre, precio)
        self.tipo_masa = tipo_masa
    
    def __str__(self):
        return f"🍞 {super().__str__()} | Masa: {self.tipo_masa}"

class Pastel(Producto):
    def __init__(self, nombre, precio, relleno):
        super().__init__(nombre, precio)
        self.relleno = relleno
    
    def __str__(self):
        return f"🎂 {super().__str__()} | Relleno: {self.relleno}"