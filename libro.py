from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas
    
    def __str__(self):
        return f"{super().__str__()} | {self.paginas} páginas"
    
    def to_dict(self):
        return {
            "tipo": "Libro",
            "titulo": self.titulo,
            "autor": self.autor,
            "paginas": self.paginas
        }