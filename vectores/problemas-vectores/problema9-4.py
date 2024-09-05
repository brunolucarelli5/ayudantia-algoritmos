"""
Problema 9.4
Diseñe un algoritmo que lea un vector desordenado A, compuesto de n enteros e imprima este vector en la
misma secuencia, pero ignorando los valores duplicados que se encuentran en él. Además se
necesita conocer la cantidad de elementos que permanecen.
Por ejemplo:
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
15 31 23 15 75 23 41 15 31 85

El vector comprimido que resulta está conformado por:
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
15 31 23 75 41 85
n = 6


Otro ejemplo
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
2   3  4 2   5  4  2  7 8  9

salida
2  3  4  5  7  8  9
"""
#vector = [2,3,4,2,5,4,2,7,8,9]



vector = [15,31,23,15,75,23,41,15,31,85]
cantidad_elementos = 10
vector_salida = [1000000000] * cantidad_elementos
indice_vector_salida = 0
vector_indices_repetidos = [-1] * cantidad_elementos # GUARDA POSICIONES DE ELEMENTOS REPETIDOS
indice_vector_indices_repetidos = 0

for i in range(cantidad_elementos):
    for j in range(cantidad_elementos):
        # si el elemento en posición i es igual al elemento en posición j, e i es diferente de j
        # además que el elemento sea distinto a -1 en ambas posiciones, significa que encontramos una repetición
        if vector[i] == vector[j] and i != j and vector[i] != 0 and vector[j] != 0:

            # guardamos el índice/posición del elemento repetido en un vector que almacena indices
            vector_indices_repetidos[indice_vector_indices_repetidos] = j
            # incrementamos en uno la posición del vector de indices, para que no se pise si encontramos otra repetición
            indice_vector_indices_repetidos += 1

        # recorremos el vector con los indices de los elementos repetidos
        for k in range(cantidad_elementos):
            # si encontramos un valor distinto a -1 significa que hay una repetición, hacemos -1
            # a ese elemento en el vector original
            if vector_indices_repetidos[k] != -1:
                vector[vector_indices_repetidos[k]] = 0
        # redefinimos el vector de indices de elementos repetidos
        vector_indices_repetidos = [-1] * cantidad_elementos
    # si el elemento es distinto a -1, lo guardamos en el vector de salida


    if vector[i] != -1:
        vector_salida[indice_vector_salida] = vector[i]
        indice_vector_salida += 1


for i in range(cantidad_elementos):
    if vector_salida[i] != 1000000000:
        print(vector_salida[i], end=' ')
