"""
El objetivo de este ejercicio es implementar un programa que verifique si los números de tarjetas de crédito son válido utilizando el algoritmo de Luhn. Este algoritmo se usa para validar una variedad de números de identificación, incluyendo números de tarjeta de crédito.

Algoritmo de Luhn:

Éste algoritmo se ejecuta de forma regresiva sobre los dígitos, es decir, en sentido inverso.

    Desde el segundo dígito (de derecha a izquierda), cada dos dígitos se duplica el valor.
        Si al duplicar el valor resulta en un número mayor que 9, se resta 9 menos dicho valor.
    Sumar todos los dígitos (incluyendo los que no se duplicaron).
    Si el total es múltiplo de 10, el número de tarjeta es válido.

-Ayuda: La cantidad de dígitos SIEMPRE es par. No debe controlarse la cantidad ni paridad.
Ejemplo:

Para la entrada: 1234567890

El algoritmo inicia desde el final, y cada 2 posiciones realiza el paso 1.
Dígito 	Se duplica? 	Nuevo valor
0 	No 	0
9 	Si 	9
8 	No 	8
7 	Si 	5
6 	No 	6
5 	Si 	1
4 	No 	4
3 	Si 	9
2 	No 	2
1 	Si 	2

Recordando que el paso 1 comenta que si al duplicar el dígito su valor es mayor que 9 se debe restar 9.

Luego se suman los nuevos dígitos como indica el paso 2, y se evalúa el paso 3.
Entrada

Lo primero que se solicitará es la cantidad de tarjetas a evaluar (n). Luego se ingresará el número completo de la tarjeta (sin espacios), ingresando una sola línea numérica por cada una de las "n" tarjetas a evaluar.

- No se controlará la cantidad de dígitos de cada tarjeta ya que éstos varían según cada compañía emisora, pero se asegura que siempre será una cantidad par. Tampoco se solicitan otros datos como CCV, vencimiento, nombres, etc.

- El algoritmo no debe detenerse hasta no permitir ingresar y evaluar cada una de las "n" tarjetas.
Salida

El programa debe mostrar al finalizar el proceso únicamente un número que represente la cantidad de tarjetas inválidas detectadas.

- No se debe mostrar más información ni escribir "Valido" e "Invalido" luego de la carga de cada tarjeta.
"""


numeroCasos = int(input())
tarjetasInvalidas = 0

for i in range(numeroCasos):
    acumulador = 0
    tarjeta = int(input())
    for j in range()



# for i in range(numeroCasos):
#     acumulador = 0
#     tarjeta = int(input())
#     for j in range(1, 25):
#         divisor = 10**j
#         digito = tarjeta % divisor
#         print("El digito que se obtiene ahora es:", digito)
#         print("Su posición es:", j)
#         if digito < 10:
#             if j % 2 == 0: # si el digito está en posicion par hacemos las operaciones
#                 print("Es índice par")
#                 aux = digito * 2
#                 if aux > 9:
#                     aux = aux - 9
#                 acumulador = acumulador + aux
#             else: # si no es indice par, sumamos al acumulador
#                 print("Es índice inpar")
#                 acumulador = acumulador + digito
#         else:
#             print("Es el último digito y sale!")
#             break
#     print(acumulador)
#     if acumulador % 10 != 0:
#         tarjetasInvalidas += 1

print(tarjetasInvalidas)