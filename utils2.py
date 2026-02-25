def somma(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("somma a,b must be int")
    return a + b

def differenza(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("differenza a,b must be int")
    return a - b

def moltiplicazione(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("prodotto a,b must be int")
    return a * b

def divisione(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("divisione a,b must be int")
    if b == 0:
        raise ZeroDivisionError("il divisore non può essere 0")
    return a / b

