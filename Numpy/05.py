#modello che predice se una persona può accedere a un prestito

# label = 0 non approvato, 1 =approvato

import numpy as np

# eta, reddito annuo, numero debiti, credit score e approvazione
np.random.seed(42)

dataset = np.array([
    [25, 30000, 2, 650, 1],
    [45, 80000, 1, 720, 1],
    [35, 50000, 5, 580, 0],
    [23, 25000, 3, 600, 0],
    [52, 120000, 0, 800, 1],
    [40, 70000, 4, 610, 0],
])

#estrarre il dato che serve per dire al nostro algoritmo, approvi il credito solo in certi casi
# impara a capire quando un finanziamento viene approvato e poi decidi tu in autonomia

X = dataset[:, :-1] #prendiamo tutte le righe e tutte le cols tranne l'ultima
Y = dataset[:, -1] #tutte le righe e solo l'ultima col (=target/label)
#features sono le prime 4, poi l'ultima è il target, label (0/1)

minimo = np.min(X, axis=0)
massimo = np.max(X, axis=0)

#normalizzazione features --> min e max si adattano a X
X_norm = (X - minimo) / (massimo - minimo)

#Feature Engineering --> creiamo nuova feature
#estraiamo una col relativa a reddito, col numero 1, poi estraiamo colonna debiti, che è col 2 e creiamo una
#nuova feature che mi dia rapporto debiti/reddito

reddito = X[:, 1]
debito = X[:, 2]
rapporto_debiti = debito / reddito  #abbiamo così un vettore

#reshape rapporto_debiti
rapporto_debiti = rapporto_debiti.reshape(-1, 1) #qui reshape perché dobbiamo avere 1 col con 6 rows

X_enhanced = np.hstack((X_norm, rapporto_debiti))

indexes = np.arange(len(X_enhanced))
np.random.shuffle(indexes) #randomizziamo il dataset

#calcoliamo elementi in training che sono l'80%
train_size = int(len(indexes) * 0.8)

train_idx = indexes[:train_size]
test_idx = indexes[train_size:]

#divido dataset in train e test sets passandogli gli indici
X_train = X_enhanced[train_idx]
X_test = X_enhanced[test_idx]

# selezioniamo i labels
Y_train = Y[train_idx]
Y_test = Y[test_idx]

#abbiamo creato 4 dataset (questi 4 sopra)
#dobbiamo passare i dati nel modello di ML in training e deve capire perché se ho questi dati mi escono questi results
#quando l'hai capito testa i dati e vedi se ti escono questi risultati
#se i risultati sono corretti, then TOP!

#usiamo la normalizzazione per normalizzare tra 0 e 1 i dati ed evitare che il modello si sbilanci