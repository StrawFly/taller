class Publicacion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"