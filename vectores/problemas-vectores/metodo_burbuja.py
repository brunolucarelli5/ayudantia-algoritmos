vector = [1, 4, 5, 2, 7, 4, 5, 8, 10, 1]

# ordenar el vector usando el método de la burbuja
for i in range(len(vector)):
    for j in range(len(vector) - 1):
        if vector[j] > vector[j + 1]:
            aux = vector[j]
            vector[j] = vector[j + 1]
            vector[j + 1] = aux
print(vector)