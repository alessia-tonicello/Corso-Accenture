f = open("dati.txt", "r")
print(f.read())
f.close()
"""
r -> lettura del file
w -> scrittura e sovrascrittura 
a -> append (aggiunge qualcosa alla fine del file)
r+ -> lettura + scrittura

apertura file -> trasformazione -> nuovo file
"""

#with open("dati.txt", "r") as f:
    # contenuto = f.read()  # oppure .readlines()

#print(contenuto)

#for line in contenuto:
    #print(line)

#with open("dati.txt", "w") as f:
    #f.write("ora distruggo tutto")


#with open("dati.txt", "a") as f:
    #f.append("ciao")


#ESERCIZIO
with open("dati.txt", "r") as f:
    nomi = f.readlines()  # oppure .readlines()

nomi_puliti =[]

for n in nomi:
    nome = n.strip()
    nome = nome.title()
    nome = nome.replace("\n","")
    nomi_puliti.append(nome)

print(nomi_puliti)

with open("dati_puliti.txt", "w") as f: #crea il file
    for nome in nomi_puliti:
        f.write(nome + "\n")
