class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni"

p1 = Persona("Ciccio", 26)
p2 = Persona("Francesca", 23)
print(p1.nome)
print(p1.eta)
print(p1.saluta())
print(p2.nome)
print(p2.eta)
