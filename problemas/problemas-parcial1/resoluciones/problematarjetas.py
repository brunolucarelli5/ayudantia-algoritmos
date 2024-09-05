"""import math

bandera = False
banderaTexto = '0'


while banderaTexto == '0':
    print('ejecutamos este codigo')

    banderaTexto = '1'
    break 


inicio = 10
fin = 10
paso = -1

for i in range(inicio,fin,paso):
    print('Ejecucion numero:', i)

for k in range(0,fin+2,1):
    print('Ejecucion numero:', k)

for i in range(1,3*2):
    print('Ejecucion numero:', i)

for i in range(6):
    print('Ejecucion numero:', i)


"""

# try {

#     tarjeta = int(input())
#     print('codigo que se ejecutará')

# } catch (EOFError) {

#   salida = 'salida'

# }


CantidadTarjetas = int(input())

r = 0

for i in range(CantidadTarjetas):
    NumTarjeta = int(input())
    h = 0
    k = 0

    acum = 0

    while NumTarjeta>0:
        digit = NumTarjeta %10
        NumTarjeta = NumTarjeta//10
        k = k+1
        digitDup = k % 2
        if  digitDup == 0:
            digit = digit * 2
            if digit > 9:
                digit = int(digit-9)
        acum = digit + acum
    valid = acum % 10
    if valid != 0:
        r = r+1
print(r)