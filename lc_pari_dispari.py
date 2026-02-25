numeri = [5, 12, 7, 20, 3, 18]

"""
creare lista che:
- divide per 2 i numeri maggiori di 10e lasci invariati gli altri 

[A if condizione else B for elemento in sequenza]
"""

lista_2 = [n / 2 if n > 10 else n for n in numeri]
print(lista_2)
