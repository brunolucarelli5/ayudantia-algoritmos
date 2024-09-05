# Pedir dimensión de matriz
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

matriz = [[0 for i in range(columnas)] for j in range(filas)]

# cargar coordenadas de premio
# fila_premio = int(input("Fila del premio: "))
# columna_premio = int(input("Columna del premio: "))
# matriz[fila_premio - 1][columna_premio - 1] = 1


# forma cargando cada elemento de la matriz
for i in range(filas):
    for j in range(columnas):
        print("Ingrese el valor de la posición (", i + 1, ", ", j + 1, "): ", end="")
        matriz[i][j] = int(input())
a
bandera = False
while bandera == False:
    # se pide la fila y columna para ver si el usuario encuentra el premio
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if matriz[fila - 1][columna - 1] == 1:
        print("SI")
        bandera = True
    else:
        print("NO")