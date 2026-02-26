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





# funzione di validazione
def validate_row(row):
    try:
        if not row["nome"].strip():
            return False, "Nome mancante"

        if not row["citta"].strip():
            return False, "Città mancante"

        eta =int(row["eta"])

        if eta < 0:
            return False, "Età non valida"

        return True, None

    except KeyError as e:
        return False, e

    except ValueError as e:
        return False, e

    except Exception as e:
        return False, e

# calcolo la categoria
def calculate_category(age):
    if age < 26:
        return "Junior"
    elif age < 30:
        return "Mid"
    else:
        return "Senior"

#pipeline

valid_users = []

try:
    with open("users.csv", newline="") as f_input, \
         open("valid_users.csv", "w", newline="") as f_valid_users, \
         open("invalid_users.csv", "w", newline="") as f_invalid_users:

        reader = csv.DictReader(f_input)
        fieldnames = reader.fieldnames if reader.fieldnames else []
        valid_fieldnames = fieldnames + ["categoria"]

        valid_writer = csv.DictWriter(f_valid_users, fieldnames = valid_fieldnames)
        invalid_writer = csv.DictWriter(f_invalid_users, fieldnames = valid_fieldnames)

        valid_writer.writeheader()
        invalid_writer.writeheader()

        for row in reader:
            is_valid, error = validate_row(row)

            if is_valid:
                eta = int(row["eta"])
                category = calculate_category(eta)

                row["categoria"] = category

                valid_writer.writerow(row)

                valid_users.append({
                    "nome": row["nome"],
                    "citta": row["citta"],
                    "eta": eta,
                    "categoria": category
                })

            else:
                row["errore"] = error
                invalid_writer.writerow(row)

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)


# salvataggio file json
try:
    with open("valid_users.json", "w" ,newline="") as f_valid_users_json:
        json.dump(valid_users, f_valid_users_json, indent=4)

except Exception as e:
    print(e)

print("Done")