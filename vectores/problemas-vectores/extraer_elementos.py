vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# extraigo elementos de la posición 3 a la 7
subvector = [0] * (7 - 3 + 1)
indice = 0
for i in range(2, 7):
    subvector[indice] = vector[i]
    indice = indice + 1
print(subvector)


# extraccion de elementos genérica
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inicio = int(input())
fin = int(input())

subvector = [0] * (fin - inicio + 1)
indice = 0
for i in range(inicio - 1, fin):
    subvector[indice] = vector[i]
    indice = indice + 1