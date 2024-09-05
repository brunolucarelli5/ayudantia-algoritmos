"""
Diseñe um algoritmo que partiendo de un vector compuesto solo por letras, debe obtener un vector
resultante cuyos elementos son solo números. La forma de obtener estos números es la siguiente:
cada posición del vector resultante será ocupada por un número que representa la cantidad de caracteres que lo
separan al caracter allí situado del más próximo caracter idéntico situado hacia su izquierda. No se
anotarán distancias superiores a 9. Cualquier caracter que no tenga hacia su izquierda otro similar a una
distancia menor o igual a 9, se le asignará un cero.

Por ejemplo, si el vector de entrada se compone de:
A A B C D B E F F E A B G B W B
El de salida será:
0 1 0 0 0 3 0 0 1 3 9 6 0 2 0 2

"""

# definimos el vector de letras y el de números, que comienza en 0
vector_letras = ['A','A','B','C','D','B','E','F','F','E','A','B','G','B','W','B'] # 16 elementos
vector_numeros = [0] * 16

# recorremos el vector de letras de derecha a izquierda
for i in range(15,-1,-1):
    # recorremos los elementos a la derecha del elemento en posición i, de derecha a izquierda 
    for j in range(i-1,-1,-1):
        # si hay repetición de letras, la diferencia entre las posiciones es menor o igual a 9
        # y en el vector de números hay algo distinto a 0, encontramos la primer repetición que buscamos
        if vector_letras[i] == vector_letras[j] and i-j <= 9 and vector_numeros[i] == 0:
            print(f"El caracter {vector_letras[i]} en la posición {i} está a {i-j} posiciones de {vector_letras[j]} en la posición {j}")
            vector_numeros[i] = i-j
print(vector_numeros)