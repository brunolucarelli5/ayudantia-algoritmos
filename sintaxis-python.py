# Python - SINTAXIS

# comentario de una línea

""" 
comentario multilínea  

tanto el comentario de una línea como el multilínea serán ignorados por el compilador
cuando se ejecute el código, por lo que podemos escribir cualquier cosa

"""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# VARIABLES

# lo de la izquierda del igual es el nombre de la variable y lo de la derecha el valor

variableEntera = 100

variableReal = -110.2

# podemos calcular variables en función de otras variables
variableCalculada = variableEntera + variableReal

variableBooleana = False

otraVariableBooleana = True

# las cadenas en python pueden ser escritas con comilla simple o comillas dobles
variableCadena = 'Hola'

otraVariableCadena = "Hola"

# podemos redefinir las variables con otros tipos de datos, por lo que hay mucha flexibilidad
variableBooleana = 'cadena'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# OPERACIONES MATEMÁTICAS Y LÓGICAS

2 + 4

2 - 4

2 * 4 # multiplicación

2 ** 4 # potencia

2 / 4 # división

2 // 4 # división entera

2 % 4 # operación módulo

'Hola' == 'Hola' # operación de igualdad

'chau' != 'chau' # operación de desigualdad

5 > 2 # mayor

5 < 2 # menor

5 >= 2 # mayor o igual

5 <= 2 # menor o igual

'Hola' == 'Hola' and 'chau' != 'chau' # operador de conjunción

'Hola' == 'Hola' or 'chau' != 'chau' # operador de disyunción

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# OPERACIONES PARA INTERACTUAR CON EL USUARIO

input() # solicitamos una entrada del usuario. por defecto será una cadena

entradaUsuario = input() # se guarda la entrada del usuario en una variable

entradaUsuario = int(input()) # se convierte la entrada del usuario en un número entero en caso que ingrese un número

entradaUsuario = float(input()) # se convierte a número con parte fraccional

print('Esto es un mensaje que se visualizará en consola') # mensajes en consola

print(variableCadena) # podemos imprimir en pantalla los valores de variables. ¡deben ser cadenas!

print('Nuestra variable tiene un valor de:', variableCadena, '. ') 
# imprimimos varios elementos a través de comas

print('Alteramos como se imprimen en pantalla varios elementos,', variableCadena, end='')
# por defecto cuando enumeramos elementos para imprimir en pantalla, Python pone un espacio entre ellos
# pero si cambiamos el parámetro end, podemos poner end = '' para que no ponga espacios o cualquier otra cosa


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# CONDICIONAL SIMPLE

notaAlumnoAlgoritmos = 6

if notaAlumnoAlgoritmos >= 6:
    print('Aprobaste el exámen.') # se ejecutará esto porque es igual a 6
else:
    print('Desaprobaste el exámen.')

notaAlumnoAlgoritmos = 2

if notaAlumnoAlgoritmos >= 6:
    print('Aprobaste el exámen.')
else:
    print('Desaprobaste el exámen.') # se ejecutará esto porque 2 es menor que 6

""" 
Python organiza el código a través de sangrías, por lo que a lo que encontramos en las líneas
106 y 108, deben estar más a la derecha de lo que tenemos en las líneas 105 y 107, respectivamente.

El condicional simple en Python se compone de
if <expresion lógica>:
    codigo que se ejecuta si <expresion logica> == True
else:
    codigo que se ejecuta si <expresion logica> == False


Podemos elegir poner el else o elegir no ponerlo. El código siguiente es válido:

if <expresion lógica>:
    codigo que se ejecuta si <expresion logica> == True

"""
    
if variableBooleana == True:
    print('codigo 1')
elif 2 > 1:
    print('codigo 2')
else:
    print('codigo 3')