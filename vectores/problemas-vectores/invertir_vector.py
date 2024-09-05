vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vector_invertido = [0] * len(vector)

otro_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
otro_vector_invertido = [0] * len(otro_vector)

# primera forma de hacerlo
for i in range(len(vector)):
    vector_invertido[i] = vector[len(vector) - 1 - i]

# segunda forma
indice = 0
for i in range(len(otro_vector) - 1, -1, -1):
    otro_vector_invertido[indice] = otro_vector[i]
    indice += 1

print('Primer vector invertido: ', vector_invertido)
print('Segundo vector invertido: ', otro_vector_invertido)