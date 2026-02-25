print("Secondo commit")

lista = ["giallo", "verde", "blu"]

for colore in lista:
    print(colore)

#numeri = [10, 20, 30]
#nuovi_numeri = []

# for numero in numeri:
#    nuovo = numero + 2
#    nuovi_numeri.append(nuovo)

# print(nuovi_numeri)

#LIST COMPREHENSION --> [trasformazione for elemento in elementi]
numeri = [1, 2, 3, 4]
quadrati = [numero ** 2 for numero in numeri]
print(quadrati)

import utils

print(utils.converti_in_maiuscolo("ciao"))



import utils2
print(utils2.divisione(12, 2))

import utils2
print(utils2.somma(12, 2))

import utils2
print(utils2.differenza(12, 2))

import utils2
print(utils2.moltiplicazione(12, 2))
