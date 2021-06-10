import os
menu=["La persona con mayor nota de las notas definitivas de los estudiantes",
"La persona con menor nota de las notas definitivas de los estudiantes","El promedio del grupo de las notas definitivas de los estudiantes",
"La cantidad de personas con nota superior al promedio","Salir"]

matriz = []
nd=list()
#lectura de datos para una matriz entera
numero_filas=int(input("ingrese la cantidad de estudiantes"))
numero_columnas=int(input("ingrese la cantidad de notas que tomo al grupo"))
notas=numero_columnas+1
for i in range(numero_filas):
    j=0
    matriz.append([])
    nombre=input("ingrese el nombre ")
    matriz[i].append(nombre)
    for j in range(1,notas,1):
        nota=float(input("ingrese la nota "))
        matriz[i].append(nota)
print(matriz)
#Calculo de notas definitivas por estudiante
for i in range(numero_filas):
    sum=0
    for j in range(1,notas,1):
        sum+=matriz[i][j]
    p=sum/numero_columnas
    nd.append(p)
print(nd)
mayor=max(nd)
menor=min(nd)
pos=nd.index(mayor)
posm=nd.index(menor)
print("El estudiante con mayor nota definitiva es ",matriz[pos][0], "su nota es ",mayor)

def inicio():
    os.system("cls")
    for i in range(len(menu)):
        print(i+1,".",menu[i])
    op=int(input("Elija una opcion"))
    if op == 1:
        print("La persona con mayor nota es ",matriz[pos][0])
        input("Presione una tecla para continuar")
    elif op ==2:
        print("La persona con mayor nota es ",matriz[posm][0])
        input("Presione una tecla para continuar")
    elif op ==3:
        sum=0
        for i in range(len(nd)):
            sum+=nd[i]
            global p
            p=sum/len(nd)
        print("El promedio es ",p)
        input("Presione una tecla para continuar")
    elif op ==4:
        c=0
        print(nd)
        for i in range(len(nd)):
            if nd[i] > p:
                c+=1
        print(c)
        input("Presione una tecla para continuar")
    else:
        exit()
inicio()