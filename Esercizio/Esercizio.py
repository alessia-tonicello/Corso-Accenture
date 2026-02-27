import csv
import json

utenti_validi3 = []

with open('requests.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        id = row["id"].strip().title()
        nome = row["nome"].strip().title()
        email = row["email"].strip().lower()
        eta = row["eta"]
        servizio = row["servizio"].strip().title()

        try:
            eta = int(eta)

            if nome != "" and "@" in email and eta >= 18:
                utenti_validi3.append(row)

                if 18 <= eta <= 25:
                    row["categoria_eta"] = "Junior"
                elif 26 <= eta <= 40:
                    row["categoria_eta"] = "Adult"
                else:
                    row["categoria_eta"] = "Senior"

        except ValueError:
            continue

print(utenti_validi3)


def organizza_dati(righe_valide):
    richieste_valide = []
    servizi_unici = set()
    conteggio_servizi = {}

    for riga in righe_valide:
        richieste_valide.append(riga)

        servizi_unici.add(riga["servizio"])

        if riga["servizio"] in conteggio_servizi:
            conteggio_servizi[riga["servizio"]] += 1
        else:
            conteggio_servizi[riga["servizio"]] = 1

    return richieste_valide, servizi_unici, conteggio_servizi


class Richiesta:
    def __init__(self, id, nome, email, eta, servizio):
        self.id = id.strip()
        self.nome = nome.strip().title()
        self.email = email.strip().lower()
        self.eta = int(eta)
        self.servizio = servizio.strip().title()

        if 18 <= self.eta <= 25:
            self.categoria_eta = "Junior"
        elif 26 <= self.eta <= 40:
            self.categoria_eta = "Adult"
        else:
            self.categoria_eta = "Senior"

    def dizionario(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "eta": self.eta,
            "servizio": self.servizio,
            "categoria_eta": self.categoria_eta
        }


class Validator:
    def validate(self,row):
        try:
            nome = row["nome"].strip().title()
            email = row["email"].strip().lower()
            eta = int(row["eta"])

            if nome == "" or "@" not in email or eta < 18:
                return False
            return True

        except (ValueError, KeyError):
            return False


class Pipeline:
    def run(self):
        richieste = []
        servizi_unici = []
        conteggio_servizi = {}

        v = Validator()

        with open('requests.csv') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if not v.validate(row):
                    continue

                request = Richiesta(
                    row["id"],
                    row["nome"],
                    row["email"],
                    row["eta"],
                    row["servizio"]
                )

                diz = request.dizionario()
                richieste.append(diz)

                servizio = diz["servizio"]
                servizi_unici.append(servizio)

                if servizio in conteggio_servizi:
                    conteggio_servizi[servizio] += 1
                else:
                    conteggio_servizi[servizio] = 1

        output = {
            "totale_richieste": len(richieste),
            "servizi_unici": list(servizi_unici),
            "conteggio_servizi": conteggio_servizi
        }

        with open('output.json', 'w', newline="") as f_out:
            json.dump(output, f_out, indent=4)



if __name__ == "__main__":
    p = Pipeline()