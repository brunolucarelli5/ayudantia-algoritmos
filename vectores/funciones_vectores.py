from ..funciones import suma, imprimir_suma


# funcion de vectores
def suma_vectores(v1, v2):
    if len(v1) == len(v2):
        suma = []
        for i in range(len(v1)):
            suma.append(v1[i] + v2[i])
        return suma
    else:
        return None
    

print(suma(1,2))