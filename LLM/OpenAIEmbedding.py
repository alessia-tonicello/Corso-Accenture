from LLM.EmbeddingModel import EmbeddingModel


class OpenAIEmbedding(EmbeddingModel):

    def genera_embedding(self, testo):
        return [1.0, 0.5, 0.3]