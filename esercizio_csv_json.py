import json
import csv

utenti_validi = []
utenti_non_validi = []

with (open("esercizio_dataset_csv_json.txt","r" , newline= "") as f):
    reader = csv.DictReader(f)

    for row in reader:
        eta = row["eta"]
        nome = row["nome"].strip()
        citta = row["citta"].strip()

        try:
            eta = int(eta)

            if eta >= 50:
                row["categoria"] = "Senior"
            elif eta >= 30:
                row["categoria"] = "Mid"
            else:
                row["categoria"] = "Junior"

            if nome and citta:
                utenti_validi.append(row)

            if not nome or not citta:
                utenti_non_validi.append(row)

        except ValueError:
            row["categoria"] = "Errore Dato"
            utenti_non_validi.append(row)

with open("utenti_validi.csv","w", newline = "") as f_input:
    col1 = ["nome", "eta", "citta", "categoria"]
    writer = csv.DictWriter(f_input, fieldnames = col1)
    writer.writeheader()
    writer.writerows(utenti_validi)

with open("utenti_non_validi.csv", "w", newline = "") as f_out:
    col2 = ["nome", "eta", "citta", "categoria"]
    writer = csv.DictWriter(f_out, fieldnames = col2)
    writer.writeheader()
    writer.writerows(utenti_non_validi)


with open("utenti2.json", "w") as f_json:
    json.dump(utenti_validi, f_json, indent=4)