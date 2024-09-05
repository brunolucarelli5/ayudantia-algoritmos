"""
ENTRADA EJEMPLO
4 6
1 2 9 9 9 9
0 0 3 9 9 9
0 0 0 0 5 9
0 0 0 0 0 6 

SALIDA EJEMPLO
S


ENTRADA EJEMPLO
5 5
1 1 2 3 4
0 1 1 4 5
0 1 2 3 6
0 0 0 2 0
0 0 0 0 0 

SALIDA EJEMPLO
N


ENTRADA EJEMPLO
5 8
0 5 1 0 3 2 2 0
0 0 0 0 4 0 1 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

SALIDA EJEMPLO
S

ENTRADA
4 4 
1 2 3 4
0 1 2 3
0 0 2 2
0 0 2 2

SALIDA
N

"""
# --------------------------------------------FUNCIONES --------------------------------------------

def crear_matriz_numeros(filas, columnas):
    matriz = [[0 for i in range(columnas)] for j in range(filas)]
    return matriz

def encontrar_dimesiones_matriz(cadena):
    for i in range(0, len(cadena)):
        if cadena[i] == " ":
            filas = int(cadena[0:i])
            columnas = int(cadena[i+1:len(cadena)])
            break
    return [filas, columnas]

def extraer_numeros_de_fila(cadena, numero_elementos):
    numeros = [0] * numero_elementos
    indice = 0
    ultimo_indice = 0
    for i in range(0, len(cadena)):
        if cadena[i] == " ":
            numeros[indice] = int(cadena[ultimo_indice:i])
            ultimo_indice = i+1
            indice += 1
    # busco el último número
    for i in range(len(cadena)-1, 0, -1):
        if cadena[i] == " ":
            cadena = cadena[i:len(cadena)]
            break
    numeros[numero_elementos-1] = int(cadena) # cargo el último elemento que no va a tener el espacio al final
    return numeros

def cargar_fila_en_matriz(matriz, fila, numeros):
    for i in range(len(numeros)):
        matriz[fila][i] = numeros[i]
    return matriz

def determinar_si_fila_tiene_solo_ceros(matriz, numero_fila):
    for i in range(len(matriz[numero_fila])):
        if matriz[numero_fila][i] != 0:
            return False
    return True

def buscar_columna_primer_elemento_distinto_cero_fila(matriz, numero_fila):
    for i in range(len(matriz[numero_fila])):
        if matriz[numero_fila][i] != 0:
            #print('Encontré el número:', matriz[numero_fila][i], 'en la columna:', i)
            return i # devuelvo el número y la columna
    return 0

def verificar_filas_debajo(matriz, fila_inicial, columna):
    for j in range(fila_inicial + 1, len(matriz)):
        for k in range(0, columna + 1):
            if matriz[j][k] != 0:
                return False
    return True

def verificar_forma_escalera(matriz, filas):
    resultado = "S"
    for i in range(filas):
        # primero verifico la primer condición para que sea escalera
        tiene_solo_ceros = determinar_si_fila_tiene_solo_ceros(matriz, i)
        if tiene_solo_ceros:
            # si la fila es todos ceros, entonces todas las filas por debajo también deben contener solo ceros
            for j in range(i + 1, filas):
                tiene_solo_ceros = determinar_si_fila_tiene_solo_ceros(matriz, j)
                if tiene_solo_ceros == False:
                    resultado = "N"
                    break
        else:
            # si la fila tiene algún número distinto de cero, entonces busco el primer número distinto de cero
            columna = buscar_columna_primer_elemento_distinto_cero_fila(matriz, i)
            # si encuentro un número distinto de cero, entonces verifico que las filas debajo tengan ceros en las columnas a la izquierda
            if verificar_filas_debajo(matriz, i, columna) == False:
                resultado = "N"
                break
        if resultado == "N":
            break
    return resultado


""" --------------------------------------- ALGORITMO PRINCIPAL --------------------------------------- """

# tomo la entrada
entrada = input()

# separo los valores de la entrada
dimensiones = encontrar_dimesiones_matriz(entrada)
filas = dimensiones[0]
columnas = dimensiones[1]

# creo la matriz
matriz = crear_matriz_numeros(filas, columnas)

for i in range(filas):
    contenido_fila = input()
    numeros_fila = extraer_numeros_de_fila(contenido_fila, columnas)  # extraigo los números de la fila
    matriz = cargar_fila_en_matriz(matriz, i, numeros_fila)  # cargo la fila en la matriz

# Verificar si la matriz tiene forma de escalera
resultado = verificar_forma_escalera(matriz, filas)

print(resultado)