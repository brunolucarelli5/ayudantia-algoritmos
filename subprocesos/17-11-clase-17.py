"""
Problema 17.11
Dada una matriz de fechas, desarrollar un algoritmo que
verifique si una fecha entrada por teclado existe en la
matriz.
Si no existe debe mostrar la más próxima indicando la
diferencia en días.
"""


# ------------------------------------- FUNCIONES ------------------------------------- #

def crear_matriz_numeros(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def calcular_dias_segun_mes(mes, año):
    dias_en_cada_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and es_bisiesto(año):
        return 29
    return dias_en_cada_mes[mes - 1]

def calcular_dias_de_año(año):
    dias = 0
    for i in range(1, año):
        dias += 366 if es_bisiesto(i) else 365
    return dias

def calcular_dias_de_fila(matriz, fila):
    dia, mes, año = matriz[fila]
    dias = dia
    for m in range(1, mes):
        dias += calcular_dias_segun_mes(m, año)
    dias += calcular_dias_de_año(año)
    return dias

def cargar_matriz_fechas(numero_fechas):
    matriz = crear_matriz_numeros(numero_fechas, 3)
    for i in range(numero_fechas):
        matriz[i][0] = int(input("Ingrese el día: "))
        matriz[i][1] = int(input("Ingrese el mes: "))
        matriz[i][2] = int(input("Ingrese el año: "))
        print("\n")
    return matriz

def calcular_dias_fecha(dia, mes, año):
    dias = dia
    for m in range(1, mes):
        dias += calcular_dias_segun_mes(m, año)
    dias += calcular_dias_de_año(año)
    return dias

def encontrar_fecha_mas_cercana(matriz, dias_fecha_calcular):
    filas = len(matriz)
    vector_dias = [0] * filas
    for i in range(filas):
        vector_dias[i] = calcular_dias_de_fila(matriz, i)
    diferencia = abs(vector_dias[0] - dias_fecha_calcular)
    indice = 0
    for i in range(filas):
        if abs(vector_dias[i] - dias_fecha_calcular) < diferencia:
            diferencia = abs(vector_dias[i] - dias_fecha_calcular)
            indice = i
    return matriz[indice], diferencia


# ------------------------------------- ALGORITMO PRINCIPAL ------------------------------------- #

def main():
    numero_fechas = int(input("Ingrese el número de fechas a cargar en la matriz: "))
    matriz = cargar_matriz_fechas(numero_fechas)

    print('Ahora se le pedirá la fecha a ingresar para calcular')
    dia_a_calcular = int(input("Ingrese el día: "))
    mes_a_calcular = int(input("Ingrese el mes: "))
    año_a_calcular = int(input("Ingrese el año: "))

    dias_fecha_calcular = calcular_dias_fecha(dia_a_calcular, mes_a_calcular, año_a_calcular)
    fecha_mas_cercana, diferencia = encontrar_fecha_mas_cercana(matriz, dias_fecha_calcular)

    print('La fecha más cercana es:', fecha_mas_cercana[0], '/', fecha_mas_cercana[1], '/', fecha_mas_cercana[2], 'con una diferencia de:', diferencia, 'días')


# ------------------------------------- LLAMADO AL ALGORITMO PRINCIPAL ------------------------------------- #

main()