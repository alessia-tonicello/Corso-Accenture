import numpy as np
from pyexpat import features

#5 persone con 4 feaures
#colonne: eta, altezza, peso, punteggio

dataset = np.random.randint(0,100, (5,4))
print(dataset)

#normalizza solo le ultime 3 colonne,
# aggiungi una nuova colonna ocn media
#crea copia dataset e verificare che non venga alterata

dataset_originale = dataset.copy()

#Normalizzazione ultime 3 colonne
features_ds = dataset[:, 1:]
print(features)

minimo = np.min(features_ds, axis=0)
massimo = np.max(features_ds, axis=0)
features_norm = (features_ds - minimo) / (massimo - minimo)

print(features_norm)
print(dataset)

#prendi posizioni di questo dataset e le sostituisci con altre cose
dataset[:, 1:] = features_norm
print(dataset)

#calcolo media features per ogni row
media_features = np.mean(dataset[: , 1:], axis=1)  #axis = 1 è perché lo voglio sulle righe, sennò era 0
media_features = media_features.reshape(-1, 1)  #-1 perché voglio col = 1 e voglio che mi trovi il numero rows
print(media_features)

#aggiungo col al dataset
dataset_con_media = np.hstack((dataset, media_features))
print(dataset_con_media)

