import json

utente = {
    "nome": "Anna"
    "eta": 22
}

with open("utente.json", "r") as f:
    dati = json.dump(utente, f, indent = 4)

print(dati["nome"])

with open("utenti.json", "r") as f_in:
    utenti= json.load(f_in)

for u in utenti:
    eta = u["eta"]

    if eta > 27:
        u["categoria"] = "Senior"
    else:
        u["categoria"] = "Junior"

print(utenti)

with open("utenti_classificati.json", "w") as f_out:
    json.dump(utenti, f_out, indent = 4)

