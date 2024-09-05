vector = [5,4,3,2,1]
print("ORDEN ORIGINAL:")
print(vector)
print("")
print("ORDENADO MEDIANTE METODO DE LA BURBUJA:")
for k in range(5):
    for n in range(k+1,5):
        if vector[k] >= vector[n]:
            guardado = vector[n]
            vector[n] = vector[k]
            vector[k] = guardado
print(vector)