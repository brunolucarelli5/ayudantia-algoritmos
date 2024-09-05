tamano_y_rondas = input()
for i in range(len(tamano_y_rondas)):
    if tamano_y_rondas[i] == " ":
        tamano = int(tamano_y_rondas[:i])
        rondas = int(tamano_y_rondas[i+1:])
        break

vector_numeros = [0] * tamano
numeros = input()
indice = 0
inicio = 0
for i in range(len(numeros)):
    if numeros[i] == " ":
        vector_numeros[indice] = int(numeros[inicio:i])
        inicio = i + 1
        indice += 1
vector_numeros[indice] = int(numeros[inicio:])
vector_salidas = [0] * rondas
indice_salidas = 0

def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = left
    pivot_index = partition(arr, left, right, pivot_index)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

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

    intervalo = [0] * (R-L+1)
    for i in range(L-1, R):
        intervalo[i-L+1] = vector_numeros[i]

    k_esimo_elemento = quickselect(intervalo, 0, len(intervalo) - 1, K - 1)

    contador = 0
    for i in range(len(intervalo)):
        if intervalo[i] == k_esimo_elemento:
            contador += 1

    salida = str(k_esimo_elemento) + " " + str(contador) + " "
    if abs(contador - G) < abs(contador - D):
        salida += "G"
    elif abs(contador - G) > abs(contador - D):
        salida += "D"
    else:
        salida += "E"
    vector_salidas[indice_salidas] = salida
    indice_salidas += 1

for i in range(rondas):
    print(vector_salidas[i])