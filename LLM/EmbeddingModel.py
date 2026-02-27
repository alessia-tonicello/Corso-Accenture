from abc import ABC, abstractmethod

class EmbeddingModel(ABC):

    @abstractmethod
    def genera_embedding(self, testo):
        pass