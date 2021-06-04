matriz=[]
opciones=["Mayor", "Menor","Promedio","cantidad"]
persona=[]
nota=[]


numero_personas=int(input("ingrese numero de estudiantes"))
numero_notas=int(input("ingrese numerro de notas"))


def menu():
        for i in range(len(opciones)):
            print(i+1,opciones[i])
            op=int(input("Ingrese la opcion"))
            if op == 1:
                print(mayor)
            elif op == 2:
                print(menor)
            elif op == 3:
                print(menor)
            else:
                print(cantidad)

            
            


def inicio():
        for i in range(numero_personas):
            
            matriz.append([])
            name=(input("Ingrese nombre del Estudiante"))
            matriz[i].append(name)
            for j in range(1,numero_notas+1,1):
                note=float(input("Ingrese la nota"))
                matriz[i].append(note)
        print(matriz)
        nod=[]
        for i in range(numero_personas):
            suma=0
            for j in range(1,numero_personas):
                suma+=matriz[i][j]
                print(suma)
                prom=suma/numero_notas
                print(i)
                
            nod[i].append(prom)
        
        print(nod)


inicio()
menu()