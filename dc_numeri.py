#DIZIONARIO
from main import quadrati

studente = {
    "nome": "Anna",
    "eta": 28,
    "corso": "Python"
}

num = [10,20,30] #lista
num_d = {
    "a": 10,
    "b": 20,
    "c": 30
}


#Dizionario da lista
quadrati = {}

for n in num:
    quadrati[n] = n*n
print(quadrati)


"""
{chave : valore for elemento in sequenza}
"""

quadrati_c = { n: n*n for n in num}
print(quadrati_c)