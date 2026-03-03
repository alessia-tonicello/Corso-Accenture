import pandas as pd

dati = {
    "nome": ["Ciccio", "Anna", "Marcello"],
    "eta": [25, 22, 38],
    "citta": ["Roma", "Milano", "Firenze"]
}

#ogni colonna è una series e ogni riga ha un indice
df = pd.DataFrame(dati)
#print(df.info())
#print(df.describe())

# df con utenti eta < 30 (seleziona colonna df[df["eta"]])
# df con utente che si chiama Anna
df_filtrato = df[df["eta"] < 30]
df_filtrato2 = df[df["nome"] == "Anna"]


dati2 = {
    "nome": ["Ciccio", "Anna", "Marcello", "Francesca", "Paolo"],
    "eta": [None, 22, 38, None, 21],
    "stipendio": [1200, 1800, None, 2100, None]
}

df2 = pd.DataFrame(dati2)
# print(df2.dropna())  # rimuove le righe con i NaN

# Sostituire tutti i dati di eta mancanti con fillna(), coon un valore standard, come 20
# ma non va bene
# df2["eta"] = df["eta"].fillna(20)
# print(df2.dropna())

#Quindi usiamo il mean per poter replace i NaN
media_eta = df2["eta"].mean()
df2["eta"] = df2["eta"].fillna(media_eta)
# df2["eta"] = df2["eta"].fillna(df2["eta"].mean()) oppure scrivi così direttamente

media_stipendio = df2["stipendio"].mean()
df2["stipendio"] = df2["stipendio"].fillna(media_stipendio)


dati3 = {
    "nome": ["Ciccio", "anna", " Marcello", "Francesca", "PAOLO"],
    "email": ["ciccio@email.com", "anna@email.com", "marcello@redyard.com", "francesca.com", None],
    "eta": [None, "22", 38, 20, 21],
    "stipendio": [1200, 1800, None, 2100, None]
}

df3 = pd.DataFrame(dati3)
#pulizia nome
df3["nome"] = df3["nome"].str.strip().str.title()

# pulizia email
df3["email"] = df3["email"].str.strip().str.lower()
df3 = df3.dropna(subset=["email"])
df3 = df3[df3["email"].str.contains("@")]

# pulizia e popolamento eta con la media
df3["eta"] = pd.to_numeric(df3["eta"], errors="coerce")  #converto eta in valore numerico
df3["eta"] = df3["eta"].fillna(df3["eta"].mean())
df3["eta"] = df3["eta"].astype(int)  #converti tutte eta in intero

# popolamento stipendio con la media
df3["stipendio"] = df3["stipendio"].fillna(df3["stipendio"].mean())


# ------------------------------------
dati4 = {
    "nome": ["Ciccio", "anna", " Marcello", "Francesca", "PAOLO"],
    "email": ["ciccio@email.com", "anna@email.com", "marcello@redyard.com", "francesca@email.com","paolo@paolo.com"],
    "eta": [25, "22", 38, 20, 21],
    "stipendio": [1200, 1800, 1900, 2100, 1750],
    "citta": ["Roma", "Milano", "Firenze", "Roma", "Roma"],
    "categoria": ["A", "A", "B", "A", "B"],
    "vendite": [240, 250, 190, 310, 370]
}

df4 = pd.DataFrame(dati4)

# raggruppare vendite per città
df4.groupby("citta")["vendite"].sum()

#vendite per categoria
df4.groupby("categoria")["vendite"].sum()

#raggruppo per più colonne
df4.groupby(["categoria", "citta"])["vendite"].sum()
print(df4)
