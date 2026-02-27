from LLM.GPTModel import GPTModel
from LLM.LocalEmbedding import LocalEmbedding
from LLM.OpenAIEmbedding import OpenAIEmbedding
from LLM.PipelineAI import PipelineAI

pipeline_1 = PipelineAI(GPTModel(), OpenAIEmbedding)
pipeline_2 = PipelineAI(GPTModel(), LocalEmbedding)

result_1 = pipeline_1.esegui("Cos'è il ML?")
result_2 = pipeline_2.esegui("Cos'è il ML?")

print(result_1)
print(result_2)