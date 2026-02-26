import json

prompt = f"""
Genera la descrizione di questo utente:
Si chiama Anna e ha 22 anni
"""
with open("utente.json", "r") as file:
    u = json.load(file)


def vincenzo_gpt(prompt, context):
    risposta = "Ciao ecco la tua descrizione: \n"
    descrizione = f"L'utente si chiama {context["nome"]} e ha {context["eta"]} anni"

    return risposta + descrizione
