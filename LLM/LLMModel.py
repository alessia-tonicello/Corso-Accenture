# Voglio che LLM risponda

from abc import ABC, abstractmethod

#Classe astratta con metodo astratto
class LLMModel(ABC):

    @abstractmethod
    # Tutte le classi che estendono questa, devono generarmi qualcosa
    def genera(self, prompt):
        pass