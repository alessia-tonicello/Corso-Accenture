from Classi.Persona import Persona

class Studente(Persona):

    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)
        self.corso = corso

    def saluta(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni e studio {self.corso}"

Ciccio = Studente("Ciccio", 25, "Python AI")
print(Ciccio.saluta())

