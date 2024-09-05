variable = 1234


while variable > 0:
    print('El numero al comienzo de la iteración es:', variable)
    digito = variable % 10
    print('El digito encontrado es:', digito)
    variable = variable // 10



variable = 1234
digito = variable // 1000 # encontramos el 1
variable = variable - digito * 1000 # sacamos el 1 y nos queda el 234 para el siguiente analisis

while variable != 0:
    digito = 