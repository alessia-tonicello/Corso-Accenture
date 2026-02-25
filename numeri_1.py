numeri = [5, 12, 26, 30, 20, 9, 14, 209]

# creare una nuova lista solo con i numeri maggiori di 10 e divisi per 2

numeri_nuovi = []

for num in numeri:
    if num > 10:
        numeri_nuovi.append(num / 2)
print(numeri_nuovi)