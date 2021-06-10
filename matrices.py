matriz=[]
numero_filas=int(input("INgrese numero de filas"))
numero_columnas=int(input("INgrese numero de filas"))
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        dato=int(input("INgrese el daro"))
        matriz[i].append(dato)
print(matriz)