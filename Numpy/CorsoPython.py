import numpy as np

numeri = [1,2,3,4]

#con numpy
array = np.array(numeri)
nuovi = array*2
print(nuovi)

numeri_random = np.random.randint(1,101, 10)
print(np.mean(numeri_random))
print(np.max(numeri_random))

"""
numeri_random = np.random.randint(1,101, 10)

.mean() --> media 
.max() --> max
"""

studenti = np.array([
    [80,79,90]
    [60,75,90]
    [88,93,90]
    [55,60,70]
])

