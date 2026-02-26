import dc_prodotti

#dataset= []

import csv
#with open('dati.csv', "w", newline = "") as csvfile:
 #   reader = csv.DictReader(csvfile)  #crea dizionari per ogni riga con chiave il nome colonna
  #  writer = csv.writer(csvfile)

   # writer.writerow(["nome", "eta", "citta"])
   # writer.writerows(["Ciccio", "19", "Ancona"])

#for row in reader:
#    dataset.append(row)
#print(dataset)


 #with open('dati.csv', "w", newline = "") as csvfile:
    #colonne = ["nome", "eta", "citta"]
    #writer = csv.DictWriter(csvfile, fieldnames=colonne)
    #writer.writeheader()
    #writer.writerow({
      #  "nome": "Mimmo",
      #  "eta": "22",
      #  "citta": "Roma"
   # })


#with open('dati.csv', newline = "") as csvfile:
    #colonne2 = ["id", "nome", "prezzo"]
    #writer = csv.DictWriter(csvfile, fieldnames=colonne2)
    #writer.writeheader()

    #for p in prodoti:
        #writer.writerow(p)

with open('dati.csv', newline = "") as f_input:
    reader= csv.DictReader(f_input)
    utenti = []
    for row in reader:
        eta = int(row["eta"])

        if eta >= 27:
            categoria = "Senior"
        else:
            categoria = "Junior"

        row["categoria"] = categoria
        utenti.append(row)
print(utenti)

with open("dati_nuovi.csv","w", newline = "") as f_input:
    colonne  = ["nome", "eta", "citta", "categoria"]
    writer = csv.DictWriter(f_input, filesname = colonne)
    writer.writeheader()

