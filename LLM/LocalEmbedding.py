from LLM.EmbeddingModel import EmbeddingModel


class LocalEmbedding(EmbeddingModel):

    def genera_embedding(self, testo):
        return [0.9, 0.1, 0.8]