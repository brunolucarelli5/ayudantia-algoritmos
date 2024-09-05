"""
Entrada
El programa recibira en la primera linea de la entrada el numero de casos de prueba. A continuacion,
cada caso de prueba estara compuesto de una unica linea que contendra un numero (positivo).

Salida
Por cada caso de prueba n, se mostrara el ultimo digito (el de la derecha) de su factorial, n!.
"""

"""
entrada de ejemplo
3
2
3
4

salida de ejemplo
2
6
4
"""


numeroCasos = int(input())
salida = ''

for i in range(numeroCasos):
    numero = int(input())
    factorial = 1
    for i in range(1, numero+1): # con este para calculamos el factorial del numero
        factorial = factorial * i 
    ultimoDigito = factorial % 10
    salida = salida + str(ultimoDigito) + "\n"

print("\n")
print(salida)