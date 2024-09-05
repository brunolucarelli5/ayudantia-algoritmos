"""
Escribir un algoritmo que determine el mayor
valor de n números enteros (diferentes) ingresados
e indicar en que posición se encuentra dicho valor.
"""

# solucion a subproblema de definir dimension e inicialización de vector
n = int(input('Ingrese la cantidad de números: '))
vector = [100000] * n

# solucion a subproblema de cargar vector con numeros
for i in range(n):
    vector[i] = int(input())

mayor = -100000000000000
# solucion a subproblema de encontrar el mayor valor y su posición
for i in range(n):
    if vector[i] > mayor:
        print('El elemento,', vector[i], 'es mayor que', mayor, 'en la posición', i)
        mayor = vector[i]
        posicion = i

print('La posicion del mayor elemento es:', posicion)