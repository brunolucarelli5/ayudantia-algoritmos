dimension = int(input())

vector = [0] * dimension

for i in range(dimension):
    vector[i] = int(input())

# variables para la secuencia con la mayor suma
inicio_maximo = 0
fin_maximo = 0
suma_maxima = 0

# variables para la secuencia actual
inicio_actual = 0
suma_actual = vector[0]

i = 1
while i < dimension:
    # Comprobamos si el valor actual es mayor que el anterior (secuencia creciente)
    if vector[i] > vector[i - 1]:
        suma_actual += vector[i]  # Añadimos el valor actual a la suma de la secuencia actual
    else:
        # Si no es creciente, verificamos si la suma de la secuencia actual es la mayor
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            inicio_maximo = inicio_actual
            fin_maximo = i - 1
        
        # Reiniciamos para la nueva secuencia
        inicio_actual = i
        suma_actual = vector[i]
    
    i += 1

# Verificamos la última secuencia en caso de que sea la de mayor suma
if suma_actual > suma_maxima:
    suma_maxima = suma_actual
    inicio_maximo = inicio_actual
    fin_maximo = dimension - 1

# se construye un vector más pequeño a partir de las posiciones y el vector original
vector_salida = [0] * (fin_maximo - inicio_maximo + 1)
for i in range(inicio_maximo, fin_maximo + 1):
    vector_salida[i - inicio_maximo] = vector[i]

# calculamos la sumatoria
sumatoria = 0
for i in range(len(vector_salida)):
    sumatoria += vector_salida[i]

print("La secuencia creciente con la mayor suma comienza en el índice", inicio_maximo, "y termina en el índice", fin_maximo)
print("Secuencia:", vector_salida)
print('Suma:', sumatoria)
