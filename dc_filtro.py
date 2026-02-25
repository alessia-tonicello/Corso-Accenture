numeri = [1,2,3,4,5,6,7,8,9]

#filtrare numeri pari e moltiplicarli per 10

pari = {n: n*10 for n in numeri if n%2==0}
print(pari)