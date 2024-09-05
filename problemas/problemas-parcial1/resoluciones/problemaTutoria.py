
# inicialización de variables para comenzar el análisis y entrar al menú de inicio del programa
finJornada = False
lugaresPlantaBaja = 50
lugaresPrimerPiso = 40
lugaresSegundoPiso = 30
autosPlantaBaja = 0
autosPrimerPiso = 0
autosSegundoPiso = 0
numeroAutosIngresaron = autosPlantaBaja + autosPrimerPiso + autosSegundoPiso
numeroPasajerosIngresaron = 0

# Mientras no termine la jornada, se ejecutará este ciclo mientras. Usamos la variable bandera finJornada.
while finJornada == False:

    # Menú principal con estadísticas
    print('')
    print('----- Estacionamiento TE CUIDAMOS EL AUTITO -----')
    print('Cartel informativo:')
    if lugaresPlantaBaja == 0:
        print('Planta baja = SIN LUGAR')
    else:
        print('Planta baja =', str(lugaresPlantaBaja)) 
        # hacemos str(lugarPiso) ya que la variable es un número. La convertimos a string para poder imprimirla en pantalla.
    if lugaresPrimerPiso == 0:
        print('Primer piso = SIN LUGAR')
    else:
        print('Primer piso =', str(lugaresPrimerPiso))
    if lugaresSegundoPiso == 0:
        print('Segundo piso = SIN LUGAR')
    else:
        print('Planta baja =', str(lugaresSegundoPiso))
    print('------------------------------------------------------')
    print('Ingrese según desee')
    print('0. Registrar ingreso de auto a estacionamiento.')
    print('1. Registrar salida de auto de estacionamiento.')
    print('2. Ver estadísticas hasta el momento de jornada.')
    print('3. Finalizar jornada y mostrar estadísticas del día.')
    print('------------------------------------------------------')

    entrada = int(input('Ingreso: '))

    # Validador de entrada de usuario para que no ingrese algo que no queremos.
    if entrada != 0 and entrada != 1 and entrada != 2 and entrada != 3:
        print('')
        print('Ingreso incorrecto, intente nuevamente.')
    else:
        # Si la entrada es correcta, analizamos con condicionales qué entrada ingresó y ejecutamos código según corresponda. 
        if entrada == 0:
            # Si la entrada es 0, hay un nuevo ingreso en el estacionamiento.
            print('')
            pasajeros = int(input('Ingrese el número de pasajeros en el auto: '))
            
            # Actualizamos el acumulador de número de pasajeros que ingresaron en la jornada.
            numeroPasajerosIngresaron = numeroPasajerosIngresaron + pasajeros

            """  
               auxiliar = entrada de usuario
               variableAcumulador <- variable + auxiliar                                          
            """ 
            
            print('¿En qué piso desea estacionar el auto?')
            if lugaresPlantaBaja != 0:
                print('0. Planta baja. =', lugaresPlantaBaja)
            else:
                print('Planta baja sin lugar disponible.')
            if lugaresPrimerPiso != 0:
                print('1. Primer piso. =', lugaresPrimerPiso)
            else:
                print('Primer piso sin lugar disponible.')
            if lugaresSegundoPiso != 0:
                print('2. Segundo piso. =', lugaresSegundoPiso)
            else:
                print('Segundo piso sin lugar disponible.')
            print('------------------------------------------------------')
            entradaPiso = int(input('Ingreso: '))
            # De acuerdo a lo que ingresa el usuario, actualizamos el contador de autos y los lugares disponibles.
            if entradaPiso == 0:
                lugaresPlantaBaja = lugaresPlantaBaja - 1
                autosPlantaBaja = autosPlantaBaja + 1
            elif entradaPiso == 1:
                lugaresPrimerPiso = lugaresPrimerPiso - 1
                autosPrimerPiso = autosPrimerPiso + 1
            elif entradaPiso == 2:
                lugaresSegundoPiso = lugaresSegundoPiso - 1
                autosSegundoPiso = autosSegundoPiso + 1
            print('Ingreso registrado correctamente! Aprete cualquier tecla para volver al menú.')
            input()
        if entrada == 1:
            # Si la entrada es 1, hay un nueva salida en el estacionamiento.
            print('')
            print('¿En qué piso estacionó el auto?')
            print('0. Planta baja.')
            print('1. Primer piso.')
            print('2. Segundo piso.')
            entradaPiso = int(input('Ingreso: '))
            # De acuerdo a lo que ingresa el usuario, actualizamos los lugares disponibles.
            if entradaPiso == 0:
                lugaresPlantaBaja = lugaresPlantaBaja + 1
            if entradaPiso == 1:
                lugaresPrimerPiso = lugaresPrimerPiso + 1
            if entradaPiso == 2:
                lugaresSegundoPiso = lugaresSegundoPiso + 1
            print('Salida de estacionamiento registrada correctamente. Gracias! Aprete cualquier tecla para salir al menú principal.')
            input()
        if entrada == 2:
            numeroAutosIngresaron = autosPlantaBaja + autosPrimerPiso + autosSegundoPiso
            # Si la entrada es 2, mostramos las estadísticas parciales.
            # Usamos las variables que se irán actualizando a medida que el usuario interactúa con el programa.
            print('')
            print('----- ESTADÍSTICAS DE JORNADA HASTA EL MOMENTO -----')
            print('Número de autos que ingresaron al estacionamiento durante la jornada =', numeroAutosIngresaron)
            print('Número de pasajeros que ingresaron al estacionamiento durante la jornada =', numeroPasajerosIngresaron)
            print('Número de autos que ingresaron a planta baja =', autosPlantaBaja)
            print('Número de autos que ingresaron a primer piso =', autosPrimerPiso)
            print('Número de autos que ingresaron a segundo piso =', autosSegundoPiso)
            print('------------------------------------------------------')
            print('Aprete cualquier tecla para salir al menú principal.')
            input()
        if entrada == 3:
            # Si la entrada es 3, significa que la jornada finalizó. Mostramos las estadísticas y finaliza el programa.
            finJornada = True
            numeroAutosIngresaron = autosPlantaBaja + autosPrimerPiso + autosSegundoPiso
            print('')
            print('Jornada finalizada correctamente. A continuación se visibilizará las estadísticas de la misma:')
            print('----- ESTADÍSTICAS DE JORNADA FINALIZADA -----')
            print('Número de autos que ingresaron al estacionamiento durante la jornada =', numeroAutosIngresaron)
            print('Número de pasajeros que ingresaron al estacionamiento durante la jornada =', numeroPasajerosIngresaron)
            print('Número de autos que ingresaron a planta baja =', autosPlantaBaja)
            print('Número de autos que ingresaron a primer piso =', autosPrimerPiso)
            print('Número de autos que ingresaron a segundo piso =', autosSegundoPiso)
            print('------------------------------------------------------')
            print('Aprete cualquier tecla para salir del programa.')
            input()


"""

definir bandera como logico

bandera <- Verdadero


mientras bandera = Verdadero hacer

    codigo que se va a ejecutar

    bajo cierta circunstancia, bandera <- Falso

finmientras


se ejecuta el resto del codigo cuando cambio el valor de la variable bandera


"""