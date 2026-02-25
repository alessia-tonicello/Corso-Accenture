temperature = [18, 22, 30, 12, 15, 32, 27, 19, 28, 20]

# crea nuova lista con temperature superiori a 20
temp_sopra_20 = []

for temp in temperature:
    if temp > 20:
        temp_sopra_20.append(temp)

    print(temp_sopra_20)