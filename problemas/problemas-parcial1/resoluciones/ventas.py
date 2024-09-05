"""Entrada
El programa recibira una lista de semanas a evaluar. Cada semana constara de un valor para cada
dia. El numero de semanas es indeterminado. El programa terminara de ejecutarse cuando para el
primer dia de la semana se indique una venta de -1."""

"""
Para cada caso de prueba, el programa escribira una linea conteniendo dos dias de la semana (MARTES,
MIERCOLES, JUEVES, VIERNES, SABADO o DOMINGO). El primero indicara el dia de mas ventas y el segundo
el de menos. Despues se indicara un SI si el domingo se realizaron mas ventas que la media semanal, y
NO en caso contrario. Las tres palabras se separaran entre ellas por un espacio.
Si hay empate en alguno de los valores de ventas minimo y maximo, se especificaria EMPATE.
"""

"""
entrada de ejemplo
185.50
250.36
163.45
535.20
950.22
450.38
-1
"""

"""
salida de ejemplo
SABADO JUEVES SI
"""

bandera = False
acumuladorMartes = 0
acumuladorMiercoles = 0
acumuladorJueves = 0
acumuladorViernes = 0
acumuladorSabado = 0
acumuladorDomingo = 0
numeroSemanas = 0

while bandera != True:
    martes = float(input())
    if martes != -1: # se verifica que las ventas del primer dia de la semana no sean -1
        acumuladorMartes = acumuladorMartes + martes
        numeroSemanas = numeroSemanas + 1
        miercoles = float(input())
        acumuladorMiercoles = acumuladorMiercoles + miercoles
        jueves = float(input())
        acumuladorJueves = acumuladorJueves + jueves
        viernes = float(input())
        acumuladorViernes = acumuladorViernes + viernes
        sabado = float(input())
        acumuladorSabado = acumuladorSabado + sabado
        domingo = float(input())
        acumuladorDomingo = acumuladorDomingo + domingo
    else:
        bandera = True

        #averiguamos los promedios de ventas de cada dia de la semana
        promedioMartes = acumuladorMartes / numeroSemanas
        promedioMiercoles = acumuladorMiercoles / numeroSemanas
        promedioJueves = acumuladorJueves / numeroSemanas
        promedioViernes = acumuladorViernes / numeroSemanas
        promedioSabado = acumuladorSabado / numeroSemanas
        promedioDomingo = acumuladorDomingo / numeroSemanas
        #calculamos la media semanal y la comparamos con las ventas de domingo
        mediaSemanal = (promedioMartes + promedioMiercoles + promedioJueves + promedioViernes + promedioSabado + promedioDomingo) / 6
        if mediaSemanal < promedioDomingo:
            domingoMedia = "SI"
        else:
            domingoMedia = "NO"

        # ahora buscaremos el dia de mayor y menor venta
        if promedioMartes > promedioMiercoles and promedioMartes > promedioJueves and promedioMartes > promedioViernes and promedioMartes > promedioSabado and promedioMartes > promedioDomingo:
            diaMayor = "MARTES"
        elif promedioMiercoles > promedioMartes and promedioMiercoles > promedioJueves and promedioMiercoles > promedioViernes and promedioMiercoles > promedioSabado and promedioMiercoles > promedioDomingo:
            diaMayor = "MIERCOLES"
        elif promedioJueves > promedioMartes and promedioJueves > promedioMiercoles and promedioJueves > promedioViernes and promedioJueves > promedioSabado and promedioJueves > promedioDomingo:
            diaMayor = "JUEVES"
        elif promedioViernes > promedioMartes and promedioViernes > promedioMiercoles and promedioViernes > promedioJueves and promedioViernes > promedioSabado and promedioViernes > promedioDomingo:
            diaMayor = "VIERNES"
        elif promedioSabado > promedioMartes and promedioSabado > promedioMiercoles and promedioSabado > promedioJueves and promedioSabado > promedioViernes and promedioSabado > promedioDomingo:
            diaMayor = "SABADO"
        else:
            diaMayor = "DOMINGO"
        
        if promedioMartes < promedioMiercoles and promedioMartes < promedioJueves and promedioMartes < promedioViernes and promedioMartes < promedioSabado and promedioMartes < promedioDomingo:
            diaMenor = "MARTES"
        elif promedioMiercoles < promedioMartes and promedioMiercoles < promedioJueves and promedioMiercoles < promedioViernes and promedioMiercoles < promedioSabado and promedioMiercoles < promedioDomingo:
            diaMenor = "MIERCOLES"
        elif promedioJueves < promedioMartes and promedioJueves < promedioMiercoles and promedioJueves < promedioViernes and promedioJueves < promedioSabado and promedioJueves < promedioDomingo:
            diaMenor = "JUEVES"
        elif promedioViernes < promedioMartes and promedioViernes < promedioMiercoles and promedioViernes < promedioJueves and promedioViernes < promedioSabado and promedioViernes < promedioDomingo:
            diaMenor = "VIERNES"
        elif promedioSabado < promedioMartes and promedioSabado < promedioMiercoles and promedioSabado < promedioJueves and promedioSabado < promedioViernes and promedioSabado < promedioDomingo:
            diaMenor = "SABADO"
        else:
            diaMenor = "DOMINGO"

# salida
print(diaMayor, diaMenor, domingoMedia)