# inicializar matriz con variables de filas y columnas
filas = int(input('Ingrese el número de filas: '))
columnas = int(input('Ingrese el número de columnas: '))

matriz = [[0 for i in range(columnas)] for j in range(filas)]

matriz_cadenas = [['' for i in range(columnas)] for j in range(filas)]


# llenar matriz
for i in range(filas):
    for j in range(columnas):
        fila = str(i + 1)
        columna = str(j + 1)
        print('Ingrese el valor de la posición (', fila,  ', ', columna, '): ', end="")
        matriz[i][j] = int(input())

print('------------------------------------------------------------------------------------------')


# Se imprime la matriz
print('Matriz ingresada:')
print(matriz)

print('------------------------------------------------------------------------------------------')

# imprimir valores en formato cuadrado
print('Impresión en formato cuadrado:')
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print()

# imprimir valores en formato lista abajo de lista
print('Impresión en forma listas apiladas:')
for i in range(filas):
    print(matriz[i])

# recorrer matriz de forma inversa
print('Se recorre la matriz de forma inversa:')
for i in range(filas-1, -1, -1):
    for j in range(columnas-1, -1, -1):
        print(matriz[i][j], end=" ")
    print()

print('------------------------------------------------------------------------------------------')


# calcular acumulador en matriz
print('Se calcula un acumulador en la matriz')
acumulador = 0
for i in range(filas):
    for j in range(columnas):
        acumulador += matriz[i][j]

print('El acumulador de la matriz es:', acumulador)

# calcular promedio de matriz
promedio = acumulador / (filas * columnas)
print('El promedio de la matriz es:', promedio)

# calcular promedio de cada fila
print('Se calcula el promedio de cada fila:')
for i in range(filas):
    acumulador = 0
    for j in range(columnas):
        acumulador += matriz[i][j]
    promedio = acumulador / columnas
    print('El promedio de la fila', i+1, 'es:', promedio)

print('------------------------------------------------------------------------------------------')