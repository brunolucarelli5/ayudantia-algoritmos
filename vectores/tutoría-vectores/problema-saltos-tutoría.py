"""
Dado un vector donde cada elemento representa el número máximo de pasos
que puedes saltar hacia adelante desde esa posición, encuentra el número
mínimo de saltos necesarios para llegar al final del vector.
Aclaración, el primer elemento del vector no puede ser 0.
"""
vector = [2, 3, 1, 1, 4]  # Ejemplo de vector
n = len(vector)

if n <= 1:
    saltos = 0  # No se necesita ningún salto si ya estamos al final
else:
    if vector[0] == 0:
        saltos = -1  # No se puede saltar desde la primera posición
    else:
        alcance = vector[0]
        pasos = vector[0]
        saltos = 1
        i = 1
        
        while i < n:
            # Si llegamos al final
            if i == n - 1:
                break
            
            if i + vector[i] > alcance:
                alcance = i + vector[i]
            
            # Usamos un paso
            pasos -= 1
            
            # Si no quedan más pasos
            if pasos == 0:
                saltos += 1
                
                # Verificamos si el salto es posible
                if i >= alcance:
                    saltos = -1  # No se puede llegar más lejos
                    break
                
                # Reestablecemos el número de pasos para el siguiente salto
                pasos = alcance - i
            
            i += 1

# Imprimir el resultado
if saltos == -1:
    print("No se puede llegar al final")
else:
    print("Número mínimo de saltos para llegar al final:", saltos)
