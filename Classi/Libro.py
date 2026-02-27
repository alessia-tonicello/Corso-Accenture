class Libro:
    def __init__(self, titolo, anno, trama):
        self.titolo = titolo
        self.anno = anno
        self.trama = trama

    def descrizione(self):
        return f"Il titolo del libro è {self.titolo}, è stato pubblicao nell'anno {self.anno} e la trama è: {self.trama}"

libro1 = Libro("Libro 1", 2025, "è un libro fantasy")
print(libro1.descrizione())