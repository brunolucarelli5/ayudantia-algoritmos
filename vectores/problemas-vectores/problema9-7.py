"""
Problema 9.7
Dado un vector que contiene enteros, diseñe un algoritmo que obtenga un nuevo vector cuyo contenido
se formará de la siguiente forma: cada elemento del nuevo vector será un índice que nos indique de menor a
mayor lo valores del vector de entrada.
"""

# definimos el vector de entrada
vector = [10, 5, -7, 0, 12]
# inicializamos variables
vector_salida = [0] * 5
indice_vector_salida = 0

# haremos el análisis de encontrar mínimos 5 veces, ya que el vector de salida tiene 5 elementos
for j in range(5):
    minimo = 100000000000
    # recorremos el vector
    for i in range(5):
        # si el elemento es menor a minimo, lo guardamos y guardamos su índice
        if vector[i] < minimo:
            minimo = vector[i]
            indice = i
    # una vez encontrado el mínimo, guardamos su posición en el vector de salida, incrementamos el indice del vector salida
    # si lo hacemos zero-based, no sumamos 1 al índice, sino sí
    vector_salida[indice_vector_salida] = indice + 1
    indice_vector_salida += 1
    # ponemos un valor grande en esa posición para que no vuelva a ser el mínimo
    vector[indice] = 100000000000
print(vector_salida)