"""
In Python, la parola chiave raise serve a sollevare (generare)
manualmente un'eccezione durante l'esecuzione di un programma
"""


def dividi(a,b):
    if b== 0:
        raise ZeroDivisionError("Il divisore non può essere 0.")
    print(dividi(a,b))

"""
Quando facciamo il Raise, possiamo fare try and except

def dividi(a,b):
    if b== 0:
        raise ZeroDivisionError("Il divisore non può essere 0.")
    return a/b
    
try:
    print(dividi(a,b))
except (ZeroDivisionError, ValueError):
    print("Division error")
"""
