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
        Escribir "Ingrese según desee";
        Escribir "0. Registrar ingreso de auto a estacionamiento.";
        Escribir "1. Registrar salida de auto de estacionamiento.";
        Escribir "2. Ver estadísticas hasta el momento de jornada.";
        Escribir "3. Finalizar jornada y mostrar estadísticas del día.";
        Escribir "------------------------------------------------------";
		
        Leer entrada;
		
        Si entrada <> 0 Y entrada <> 1 Y entrada <> 2 Y entrada <> 3 Entonces
            Escribir "";
            Escribir "Ingreso incorrecto, intente nuevamente.";
        SiNo
            Si entrada = 0 Entonces
                Escribir "";
                Escribir "Ingrese el número de pasajeros en el auto:";
                Leer pasajeros;
                numeroPasajerosIngresaron <- numeroPasajerosIngresaron + pasajeros;
                Escribir "¿En qué piso desea estacionar el auto?";
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
                Escribir "Ingreso registrado correctamente! Aprete cualquier tecla para volver al menú.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 1 Entonces
                Escribir "";
                Escribir "¿En qué piso estacionó el auto?";
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
                Escribir "Salida de estacionamiento registrada correctamente. Gracias! Aprete cualquier tecla para salir al menú principal.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 2 Entonces
                Escribir "";
                Escribir "----- ESTADÍSTICAS DE JORNADA HASTA EL MOMENTO -----";
                Escribir "Número de autos que ingresaron al estacionamiento durante la jornada =", autosPlantaBaja + autosPrimerPiso + autosSegundoPiso;
                Escribir "Número de pasajeros que ingresaron al estacionamiento durante la jornada =", numeroPasajerosIngresaron;
                Escribir "Número de autos que ingresaron a planta baja =", autosPlantaBaja;
                Escribir "Número de autos que ingresaron a primer piso =", autosPrimerPiso;
                Escribir "Número de autos que ingresaron a segundo piso =", autosSegundoPiso;
                Escribir "------------------------------------------------------";
                Escribir "Aprete cualquier tecla para salir al menú principal.";
                Leer _tecla;
            FinSi;
			
            Si entrada = 3 Entonces
                finJornada <- Verdadero;
                Escribir "";
                Escribir "Jornada finalizada correctamente. A continuación se visibilizará las estadísticas de la misma:";
                Escribir "----- ESTADÍSTICAS DE JORNADA FINALIZADA -----";
                Escribir "Número de autos que ingresaron al estacionamiento durante la jornada =", autosPlantaBaja + autosPrimerPiso + autosSegundoPiso;
                Escribir "Número de pasajeros que ingresaron al estacionamiento durante la jornada =", numeroPasajerosIngresaron;
                Escribir "Número de autos que ingresaron a planta baja =", autosPlantaBaja;
                Escribir "Número de autos que ingresaron a primer piso =", autosPrimerPiso;
                Escribir "Número de autos que ingresaron a segundo piso =", autosSegundoPiso;
                Escribir "------------------------------------------------------";
                Escribir "Aprete cualquier tecla para salir del programa.";
                Leer _tecla;
            FinSi;
        FinSi;
    FinMientras;

FinProceso
