#LIST COMPREHENSION

#traforma ogni numero aggiungendo 5 al numero irigine

numeri = [10, 20, 30]  #aggiugi 5 ad ogni num

nuovi = [numero + 5 for numero in numeri]

## filtrare con le list comprehension
# [trasformazione for elemento in elementi if condizione]

numeri_2 = [1,2,3,4,5,6,7,8,9]
numeri_pari = [numero for numero in numeri_2 if numero % 2 == 0]
print(numeri_pari)

## trasformazione + filtraggio
# numeri pari moltiplicati per 10

numeri_pari_x_10 = [numero * 10 for numero in numeri_2 if numero % 2 == 0]
print(numeri_pari_x_10)

