Proceso Estacionamiento
	
    Definir finJornada Como Logico;
	Definir _tecla Como Caracter;
    Definir lugaresPlantaBaja, lugaresPrimerPiso, lugaresSegundoPiso Como Entero;
    Definir autosPlantaBaja, autosPrimerPiso, autosSegundoPiso Como Entero;
    Definir numeroPasajerosIngresaron, entrada, pasajeros, entradaPiso Como Entero;
	
    finJornada <- Falso;
    lugaresPlantaBaja <- 50;
    lugaresPrimerPiso <- 40;
    lugaresSegundoPiso <- 30;
    autosPlantaBaja <- 0;
    autosPrimerPiso <- 0;
    autosSegundoPiso <- 0;
    numeroPasajerosIngresaron <- 0;
	
    Mientras finJornada = Falso Hacer
        Escribir "";
        Escribir "----- Estacionamiento TE CUIDAMOS EL AUTITO -----";
        Escribir "Cartel informativo:";
        Si lugaresPlantaBaja = 0 Entonces
            Escribir "Planta baja = SIN LUGAR";
        SiNo
            Escribir "Planta baja =", lugaresPlantaBaja;
        FinSi;
        Si lugaresPrimerPiso = 0 Entonces
            Escribir "Primer piso = SIN LUGAR";
        SiNo
            Escribir "Primer piso =", lugaresPrimerPiso;
        FinSi;
        Si lugaresSegundoPiso = 0 Entonces
            Escribir "Segundo piso = SIN LUGAR";
        SiNo
            Escribir "Segundo piso =", lugaresSegundoPiso;
        FinSi;
        Escribir "------------------------------------------------------";
        Escribir "Ingrese seg�n desee";
        Escribir "0. Registrar ingreso de auto a estacionamiento.";
        Escribir "1. Registrar salida de auto de estacionamiento.";
        Escribir "2. Ver estad�sticas hasta el momento de jornada.";
        Escribir "3. Finalizar jornada y mostrar estad�sticas del d�a.";
        Escribir "------------------------------------------------------";
		
        Leer entrada;
		
        Si entrada <> 0 Y entrada <> 1 Y entrada <> 2 Y entrada <> 3 Entonces
            Escribir "";
            Escribir "Ingreso incorrecto, intente nuevamente.";
        SiNo
            Si entrada = 0 Entonces
                Escribir "";
                Escribir "Ingrese el n�mero de pasajeros en el auto:";
                Leer pasajeros;
                numeroPasajerosIngresaron <- numeroPasajerosIngresaron + pasajeros;
                Escribir "�En qu� piso desea estacionar el auto?";
                Si lugaresPlantaBaja <> 0 Entonces
                    Escribir "0. Planta baja =", lugaresPlantaBaja;
                SiNo
                    Escribir "Planta baja sin lugar disponible.";
                FinSi;
                Si lugaresPrimerPiso <> 0 Entonces
                    Escribir "1. Primer piso =", lugaresPrimerPiso;
                SiNo
                    Escribir "Primer piso sin lugar disponible.";
                FinSi;
                Si lugaresSegundoPiso <> 0 Entonces
                    Escribir "2. Segundo piso =", lugaresSegundoPiso;
                SiNo
                    Escribir "Segundo piso sin lugar disponible.";
                FinSi;
                Escribir "------------------------------------------------------";
                Leer entradaPiso;
                Si entradaPiso = 0 Entonces
                    lugaresPlantaBaja <- lugaresPlantaBaja - 1;
                    autosPlantaBaja <- autosPlantaBaja + 1;
                FinSi;
                Si entradaPiso = 1 Entonces
                    lugaresPrimerPiso <- lugaresPrimerPiso - 1;
                    autosPrimerPiso <- autosPrimerPiso + 1;
                FinSi;
                Si entradaPiso = 2 Entonces
                    lugaresSegundoPiso <- lugaresSegundoPiso - 1;
                    autosSegundoPiso <- autosSegundoPiso + 1;
                FinSi;
                Escribir "Ingreso registrado correctamente! Aprete cualquier tecla para volver al men�.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 1 Entonces
                Escribir "";
                Escribir "�En qu� piso estacion� el auto?";
                Escribir "0. Planta baja.";
                Escribir "1. Primer piso.";
                Escribir "2. Segundo piso.";
                Leer entradaPiso;
                Si entradaPiso = 0 Entonces
                    lugaresPlantaBaja <- lugaresPlantaBaja + 1;
                FinSi;
                Si entradaPiso = 1 Entonces
                    lugaresPrimerPiso <- lugaresPrimerPiso + 1;
                FinSi;
                Si entradaPiso = 2 Entonces
                    lugaresSegundoPiso <- lugaresSegundoPiso + 1;
                FinSi;
                Escribir "Salida de estacionamiento registrada correctamente. Gracias! Aprete cualquier tecla para salir al men� principal.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 2 Entonces
                Escribir "";
                Escribir "----- ESTAD�STICAS DE JORNADA HASTA EL MOMENTO -----";
                Escribir "N�mero de autos que ingresaron al estacionamiento durante la jornada =", autosPlantaBaja + autosPrimerPiso + autosSegundoPiso;
                Escribir "N�mero de pasajeros que ingresaron al estacionamiento durante la jornada =", numeroPasajerosIngresaron;
                Escribir "N�mero de autos que ingresaron a planta baja =", autosPlantaBaja;
                Escribir "N�mero de autos que ingresaron a primer piso =", autosPrimerPiso;
                Escribir "N�mero de autos que ingresaron a segundo piso =", autosSegundoPiso;
                Escribir "------------------------------------------------------";
                Escribir "Aprete cualquier tecla para salir al men� principal.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 3 Entonces
                finJornada <- Verdadero;
                Escribir "";
                Escribir "Jornada finalizada correctamente. A continuaci�n se visibilizar� las estad�sticas de la misma:";
                Escribir "----- ESTAD�STICAS DE JORNADA FINALIZADA -----";
                Escribir "N�mero de autos que ingresaron al estacionamiento durante la jornada =", autosPlantaBaja + autosPrimerPiso + autosSegundoPiso;
                Escribir "N�mero de pasajeros que ingresaron al estacionamiento durante la jornada =", numeroPasajerosIngresaron;
                Escribir "N�mero de autos que ingresaron a planta baja =", autosPlantaBaja;
                Escribir "N�mero de autos que ingresaron a primer piso =", autosPrimerPiso;
                Escribir "N�mero de autos que ingresaron a segundo piso =", autosSegundoPiso;
                Escribir "------------------------------------------------------";
                Escribir "Aprete cualquier tecla para salir del programa.";
                Leer _tecla;
            FinSi;
        FinSi;
    FinMientras;

FinProceso
