numeri = [1,2,3,4,5,6,7,8,9]

#scelta tra 2 trasformazioni la struttura cambia
#esempio: stampa collection che dice se num è pari o dispari

# SINTASSI:
# [A if condizione else B for elemento in sequenza]

risultato = ["pari" if numero % 2 == 0 else "dispari" for numero in numeri]
print(risultato)

# non usiamo lc quado logica coplessa, troppi if, quando codice diventa difficile
# e se serve fare debugging (soluzione = funzione)