from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato**2

class Cerio(Forma):

    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return self.raggio**2 * 3.14

"""
Ereditarietà --> Q and C ereditano area da Forma, che è un contratto astratto
Polimorfismo --> Q and C lo fanno ma in modo diverso 
"""