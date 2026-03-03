import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

pd.options.display.max_columns = 8
pd.options.display.max_rows = 100
df = pd.read_csv("Titanic-Dataset.csv")

df["IsMaleChild"] = 0
df.loc[df["Name"].str.contains("Master"), "IsMaleChild"] = 1

survived = df["Survived"].value_counts()
survived_by_sex = df.groupby("Sex")["Survived"].mean()
survived_by_class = df.groupby("Pclass")["Survived"].mean()

avg_age_survived = df[df["Survived"] == 1]["Age"].mean()

survived_by_age = df.groupby("Age")["Survived"].mean()

#prezzo medio e massimo per classe
df.groupby("Pclass")["Fare"].mean()
df.groupby("Pclass")["Fare"].max()

"""
Classe e sex sono importanti più che l'età
"""

# Un modello ML vuole solo numeri e colonne relevant

df = df.drop(["Name", "Cabin", "Ticket", "PassengerId", "Fare"], axis = 1) #eliminiamo alcune colonne (quindi axis = 1)

#riempiamo eta con mean values
df["Age"] = df["Age"].fillna(df["Age"].median())

#fill embarked con porto più frequente
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#crea nuova feature
df["FamilySize"] = df["SibSp"] + df["Parch"] +1
df.loc[df["FamilySize"] == 1, "IsAlone"] = 1   # loc() assegna valori condizionali
df.drop(["SibSp", "Parch"], axis = 1)

df["IsAlone"] = 0


df["Age0015"] = 0
df["Age1540"] = 0
df["Age4080"] = 0

# Usa l'operatore & (and) e racchiudi le condizioni tra parentesi
df.loc[(df["Age"] > 0) & (df["Age"] <= 15), "Age0015"] = 1
df.loc[(df["Age"] > 15) & (df["Age"] <= 40), "Age1540"] = 1
df.loc[df["Age"] > 40, "Age4080"] = 1

df = df.drop(["Age"], axis = 1)

# One hot encoding
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

#due dataset: uno con le features (X) e poi l'altro è il dataset y con dati target (Survived)
X = df.drop("Survived", axis = 1)
y = df["Survived"]


#SEPARAZIONE NEI 4 SETS --> train e test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# CLASSIFICAZIONE BINARIA --> LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test) #fa la prediction sul test set
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy ------>", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix ------>")
print(cm)

cr = classification_report(y_test, y_pred)
print("Classification Report ------>")
print(cr)


y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("Train Accuracy ------>", train_accuracy)
print("Test Accuracy ------>", test_accuracy)


for feature, coef in zip(X.columns, model.coef_[0]):
    print(feature, coef)


jack = {
    "Pclass": 3,
    "IsMaleChild": 0,
    "FamilySize": 1,
    "IsAlone": 1,
    "Sex_male": 1,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1,
}

rose = {
    "Pclass": 1,
    "IsMaleChild": 0,
    "FamilySize": 2,
    "IsAlone": 0,
    "Sex_male": 0,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1,
}

vince = {
    "Pclass": 2,
    "IsMaleChild": 0,
    "FamilySize": 4,
    "IsAlone": 0,
    "Sex_male": 1,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q": 0,
    "Embarked_S": 0,
}

char_titanic_movie = pd.DataFrame([jack, rose, vince], index = ["Jack", "Rose", "Vince"])
char_titanic_movie = char_titanic_movie.reindex(columns=X.columns, fill_value=0)

pred_class = model.predict(char_titanic_movie)
pred_proba = model.predict_proba(char_titanic_movie)[:, 1]

results = pd.DataFrame(
    {
        "Predicted Survived": pred_class,
        "Predicted Probability": pred_proba,
    }, index= char_titanic_movie.index
)

print(results)

from matplotlib import pyplot as plt
survived_by_sex = df.groupby("Sex_male")["Survived"].mean()

plt.figure()
plt.bar(["Femminucce", "Maschietti"], survived_by_sex)
plt.title("Sopravvivenza per Sesso")
plt.ylabel("% Sopravvivenza")
plt.xlabel("Sesso")
plt.show()
