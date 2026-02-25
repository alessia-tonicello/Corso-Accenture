"""
Scrivere una pipeline che
- riceve una lista di stringhe numeriche
- li converte in interi gestendo gli errori
- restituisce solo i > 10
- calcola la somma sum(list)
"""
dati = ["1", "2", "3", "4"]

def convertire_in_interi(lista):
    interi = []
    for n in lista:
    try:
        interi.append(int(n))
    except ValueError:
        pass
    return interi

print(convertire_in_interi("1"))


def i_maggiore_10(lista):
    return [n for n in lista if n > 10]


def somma(lista):
        return sum(lista)
