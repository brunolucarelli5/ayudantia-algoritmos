"""

Generalmente, cuando una competencia de programación termina, los participantes suelen interactuar. En base a ello, Rangel está desarrollando un juego para que los participantes se entretengan después de una competencia. Este juego se conocerá como “El Juego del Vector”.

El Juego del Vector funciona de la siguiente manera:

    Se genera un vector de N enteros aleatorios y se muestra a los jugadores durante 10 segundos.
    Luego se realizan Q rondas, donde los jugadores deben decir cuántas veces aparece el K-ésimo elemento más pequeño dentro de un intervalo dado del vector.
    Gana la ronda aquel jugador que dijo el número más cercano al resultado correcto.

Este año, Rangel llamó a sus amigos Guille y Damián para probar el nuevo juego y te pidió que diseñaras el algoritmo para indicar cuál es la frecuencia de aparición del K-ésimo elemento más pequeño en el intervalo y quién es el ganador de la ronda.
Entrada

La primer línea consta de dos enteros N y Q (1 ≤ N, Q ≤ 1000) que representan el tamaño del arreglo y la cantidad de rondas respectivamente. La siguiente línea contiene N enteros Xi (1 ≤ Xi ≤ 232-1) que son los elementos del arreglo. Las siguientes Q líneas contienen 5 enteros L y R(1 ≤ L ≤ R ≤ N) que representan los extremos del intervalo de la ronda, K que es el K-ésimo elemento más pequeño del intervalo (siempre existe), G y D (1 ≤ G, D ≤ 232-1) que son los valores indicados por Guille y Damián respectivamente.
Salida

Por cada ronda vas a tener que imprimir un entero X que es el K-ésimo elemento más pequeño del intervalo, un entero Y que indica cuántas veces apareció el K-ésimo elemento más pequeño en el intervalo y un caracter C que debería ser uno de los siguientes:

    G si gana Guille;
    D si gana Damián;
    E si hay empate.

EJEMPLO DE ENTRADA:

10 5
1 4 5 2 7 4 5 8 10 1
1 10 1 3 1
1 5 2 1 4
2 6 3 1 1
7 7 1 0 10
3 8 4 10 4  

SALIDA:

1 2 E
2 1 G
4 2 E
5 1 G
5 2 D

"""

tamano_y_rondas = input()
for i in range(len(tamano_y_rondas)):
    if tamano_y_rondas[i] == " ": # voy obteniendo los números a partir de subcadena y los espacios
        tamano = int(tamano_y_rondas[:i])
        rondas = int(tamano_y_rondas[i+1:])
        break

vector_numeros = [0] * tamano
numeros = input()
indice = 0
inicio = 0
for i in range(len(numeros)):
    if numeros[i] == " ": # lo mismo que arriba pero para el vector de números y con acumulador para el índice
        vector_numeros[indice] = int(numeros[inicio:i])
        inicio = i + 1
        indice += 1
# Para el último número después del último espacio
vector_numeros[indice] = int(numeros[inicio:])
vector_salidas = [0] * rondas
indice_salidas = 0

# ahora se buscar L, R, K, G y D
for i in range(rondas):
    valores = input()
    for j in range(len(valores)):
        if valores[j] == " ":
            L = int(valores[:j])
            inicio = j + 1
            break
    for j in range(inicio, len(valores)):
        if valores[j] == " ":
            R = int(valores[inicio:j])
            inicio = j + 1
            break
    for j in range(inicio, len(valores)):
        if valores[j] == " ":
            K = int(valores[inicio:j])
            inicio = j + 1
            break
    for j in range(inicio, len(valores)):
        if valores[j] == " ":
            G = int(valores[inicio:j])
            inicio = j + 1
            break
    D = int(valores[inicio:])

    # ahora que tengo los valores de la ronda, debo buscar el K-ésimo elemento más pequeño en el intervalo
    # para ello, debo ordenar el intervalo y buscar el K-ésimo elemento
    intervalo = [0] * (R-L+1)
    for i in range(L-1, R):
        intervalo[i-L+1] = vector_numeros[i]
    
    # se ordena el intervalo con método de burbuja
    for i in range(len(intervalo)):
        for j in range(len(intervalo)-1):
            if intervalo[j] > intervalo[j+1]:
                aux = intervalo[j]
                intervalo[j] = intervalo[j+1]
                intervalo[j+1] = aux
    
    #print(intervalo)
    #print(intervalo[K-1])

    # agrego la primer respuesta a la salida
    salida = str(intervalo[K-1]) + " "
    # ahora debo contar cuántas veces aparece el K-ésimo elemento en el intervalo
    contador = 0
    for i in range(len(intervalo)):
        if intervalo[i] == intervalo[K-1]:
            contador += 1
    # agrego la segunda respuesta a la salida
    salida += str(contador) + " "
    #print(contador)
    # ahora debo determinar quién es el ganador de la ronda
    if abs(contador - G) < abs(contador - D):
        salida = salida + "G"
    elif abs(contador - G) > abs(contador - D):
        salida = salida + "D"
    else:
        salida = salida + "E"
    vector_salidas[indice_salidas] = salida
    indice_salidas += 1
for i in range(rondas):
    print(vector_salidas[i])