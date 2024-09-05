# CÓMO DEFINIR UN VECTOR EN PYTHON

dimension = 3  # numero entero
vector_numeros = [0] * dimension
vector_letras = [''] * dimension
vector_booleanos = [False] * dimension

primer_elemento = vector_numeros[0]
ultimo_elemento = vector_numeros[dimension - 1]

# recorrer un vector
for i in range(dimension):
    vector_numeros[i] = int(input(f'Ingrese el número {i + 1}: '))


# recorrer un vector de atras para adelante
for i in range(dimension - 1, -1, -1):
    print(vector_numeros[i])

# recorrer un vector usando ciclo while/mientras
i = 0
while i < dimension:
    print(vector_numeros[i])
    i += 1
