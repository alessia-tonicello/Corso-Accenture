import numpy as np

x = 5

v = np.array([1,2,3,4,5])

print(v.shape)

m = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(m.shape)

t = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(t.shape)

a = np.array([1,2,3,4,5])
b = 10

print(a+b)

"""
Numpy espande b, che non ha dimensioni e lo adatta alla dimensione di a, senza creare l'array di b in memoria.
Questo si chiama broadcasing.
"""

a = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
b = np.array([10,20,30])
print(a+b)

media = np.mean(a, axis=0)
norm = a - media

print(norm)


# Reshaping --> si può fare mantenendo lo stesso numero di elementi
c = np.array([1,2,3,4,5,6])
#d = np.array(
   # [
    #[1,2,3],
   # [4,5,6]
    #]
#)

d = c.reshape(2,3)
print(d)

c2 = np.array([1,2,3,4,5,6,3,4,5,6,6,4,5,7,5,2,6,7,42,4,5,3,6])
d1 = c.reshape(3,-1)
print(d1)

a2 = np.array([1,2,3,4,5,6,3,4,5,6,6,4,5,7,5,2,6,7,42,4,5,3,6])
b2 = a[0:2].copy()
b2[0] = 99
print(b2)
print(a2)