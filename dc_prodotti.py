prodotti = [
    {"id":1, "nome":"PC", "prezzo": 999.00},
    {"id": 2, "nome": "Monitor", "prezzo": 699.00},
    {"id":3, "nome":"Mouse", "prezzo": 99.00},
    {"id":4, "nome":"Tastiera", "prezzo": 129.00},
]

#chiave 1 = id 1
indice = {p["id"]: p for p in prodotti}

print(indice)
