numeri = [3,6,9,12,15,18,21,24,27,30]

"""
creare dizionario
- chiave -> numero
- valore -> numero diviso 3
"""

num_diviso_3 = {num: num / 3 for num in numeri}
print(num_diviso_3)


nomi = ["Anna", "Ciccio", "Francesca", "Annibale"]
"""
creare dizionario
- chiave -> nome
- valore -> lungo se la lun > 5, altrimenti corto
"""

lun = {nome: "Lungo" if len(nome) > 5 else "Corto" for nome in nomi}
print(lun)