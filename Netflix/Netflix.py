import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


pd.options.display.max_rows = 20
pd.options.display.max_columns = 20

# TF IDF
df = pd.read_csv("Netflix.csv")

# Strategia --> creare una colonna soup che concatena director + cast + genre + description

# Fine: Modello di predizione utilizzando le colonne SOUP e TD IDF

df = pd.DataFrame(df)

df.fillna('', inplace=True)

missing_values = df.isnull().sum()
# print(missing_values)


cols1 = ["director", "cast", "country", "genres", "description"]
for col in cols1:
    df[cols1] = df[cols1].astype(str)


df["Soup"] = (
    df["director"] + " " +
    df["cast"] + " " +
    df["country"] + " " +
    df["genres"] + " " +
    df["description"]
)

def clean_data(text):
    if isinstance(text, str):
        return text.lower()
    else:
        return ""

df["Soup"] = df["Soup"].apply(clean_data)

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df["Soup"])


# Nearest Neighbors
model = NearestNeighbors(
    n_neighbors= 11,
    metric="cosine",
    algorithm="brute",
)

model.fit(tfidf_matrix)


# Funzione di raccomandazione
def recommend_by_title(
        title: str,
        k: int = 10,
        same_genre: bool = False,
) -> pd.DataFrame:

    seed = df[df["title"] == title]

    if seed.empty:
        raise ValueError("Title does not exist")

    idx = seed.index[0]

    seed_vec = tfidf_matrix[idx]

    distances, indices = model.kneighbors(seed_vec)

    recs = df.iloc[indices[0]].copy()

    # rimuoviamo il film seed
    recs = recs[recs["title"] != title]

    seed_genres = [g.strip() for g in seed.iloc[0]["genres"].split(",")]
    recs = recs[recs["genres"].apply(lambda x: any(g in x for g in seed_genres))]


    recs = recs.head(k)

    cols = [
        "title",
        "director",
        "genres",
        "country",
        "description"
    ]

    return recs[cols]



test_title = "The Witcher"
print("Film seed: \n")
print(df[df["title"] == test_title][["title", "director", "genres", "country", "description"]])

print("Film consigliati:\n")
print(recommend_by_title(test_title, k=10, same_genre= True))