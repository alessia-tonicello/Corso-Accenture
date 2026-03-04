import pandas as pd
import numpy as np
from pandas.conftest import ascending
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors  #cerca le canzoni più vicine a quelle che passiamo

pd.options.display.max_rows = 20
pd.options.display.max_columns = 20

df = pd.read_csv("dataset.csv")
# print("Righe totali: ", len(df))
# print("Tracce Uniche:", df["track_id"].nunique())

missing = df.isna().sum().sort_values(ascending=False)
# print(missing)

missing_values = df.isnull().sum()
# print(missing_values)


#Features numeriche
feature_num = [
    "energy",
    "tempo",
    "valence",
    "acousticness"
]

df = df.sort_values("popularity", ascending = False)
df = df.drop_duplicates(subset = ["track_id"], keep = "first")

# ONE HOT ENCODING per genre
genre_ohe = pd.get_dummies(df["track_genre"], prefix="genre")


#Normalizzazione dei dati

X_num = df[feature_num]

#aggiungiamo genre qui
X = pd.concat([X_num, genre_ohe], axis = 1)

scaler = StandardScaler()

X_num_scaled = scaler.fit_transform(X_num)
X_final = np.hstack((X_num_scaled, genre_ohe.values))

print(X_final.shape)

#Nearest Neighbors cerca i records + vicini a quello spazio
model = NearestNeighbors(
    n_neighbors= 10+1,
    metric="euclidean"
)

# fit in questo caso memorizza i punti e costruisce una struttura per cercare le canzoni vicine + velocemente
model.fit(X_final)


# FUNZIONE DI RACCOMANDAZIONE -- passiamo il track_id e lui ci trova le canzoni più simili
# la funzione prende features del dataset, cerca nella matrice le 10 canzoni più vicini e le suggerisce
def recommend_by_track_id(
        track_id: str,
        k: int = 10,
        same_genre: bool = False,
) -> pd.DataFrame:

    seed = df[df["track_id"] == track_id]
    if seed.empty:
        raise ValueError("Track ID does not exist")

    seed_row = seed.iloc[0]

    seed_num = seed[feature_num]
    seed_num_scaled = scaler.transform(seed_num)

    seed_genre = seed_row["track_genre"]
    seed_genre_ohe = np.zeros((1, genre_ohe.shape[1]))

    genre_col_name = f"genre_{seed_genre}"

    if genre_col_name in genre_ohe.columns:
        idx = list(genre_ohe.columns).index(genre_col_name)
        seed_genre_ohe[0, idx] = 1

    seed_vec = np.hstack([seed_num_scaled, seed_genre_ohe])

    # per cercare i vicini usiamo una tupla
    distances, indices = model.kneighbors(seed_vec)

    #recuperiamo righe da daaset principali di raccomandazioni
    recs = df.iloc[indices[0]].copy()

    recs = recs[recs["track_id"] != track_id]  #eliminiamo da recs la traccia seed

    if same_genre:
        seed_genre = seed.iloc[0]["genres"]
        recs = recs[recs["genres"] == seed_genre]

    recs = recs.head(k)

    cols = [
        "track_id",
        "track_name",
        "artists",
        "track_genre",
        "popularity"
    ]

    return recs[cols]


test_id = "4nVBt6MZDDP6tRVdQTgxJg"
print("Traccia seed: \n")
print(df[df["track_id"] == test_id][["track_name", "artists", "track_genre"]])

print("Tracce consigliate: \n")
print(recommend_by_track_id(test_id, k=10, same_genre=True))