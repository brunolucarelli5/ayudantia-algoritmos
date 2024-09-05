"""
Problema 9.6
Dado un polinomio p(x) = a0 + a1x + a2x^2 + ... + anx^n, donde a0, a1, a2, ..., an
son números reales que indican los coeficientes del polinomio, diseñe un algoritmo que lea n, seguido de
estos coeficientes y una secuencia de valores de x. Para cada uno de estos valores de x, debe calcularse el
valor de p(x).
"""

# inicialización de variables
vector_salidas = [0] * 100
indice_vector_salidas = 0
salida = False
resultado = 0
n = int(input("Ingrese el grado del polinomio: "))

# consideramos que vamos a tener n+1 coeficientes
# creamos el vector
coeficientes = [0] * (n+1)
for i in range(n+1):
    coeficientes[i] = float(input(f"Ingrese el coeficiente a{i}: "))

while salida != True:
    print('¿Desea ingresar un nuevo valor de x?')
    print('1. Sí')
    print('2. No')
    entrada = int(input())
    if entrada == 1:
        # cargamos el vector con los coeficientes
        x = float(input("Ingrese el valor de x: "))
        exponente = n

        for i in range(n+1):
            resultado = resultado + coeficientes[i] * x ** exponente
            #print(coeficientes[i], "*", x, "^", exponente, "=", coeficientes[i] * x ** exponente)
            exponente = exponente - 1
        print(resultado)
        vector_salidas[indice_vector_salidas] = resultado
        indice_vector_salidas += 1
    if entrada == 2:
        salida = True

print(vector_salidas)

for i in range(100):
    if vector_salidas[i] != 0:
        print(vector_salidas[i], end=' ')