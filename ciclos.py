import os
import time
#Lista con las opciones del menu
menu=["Salir","Saludar","Es Par","Promedio","Modulo","Porcentaje","Potencia"]

#Ciclo para recorrer la lista y generar la ocpiones del menu
print("====================")
print("Menu de opciones")
print("====================\n")

def salir():
    exit("Bye")

def saludar():
    os.system("cls")
    hora=int((time.strftime("%H", time.localtime()) ))
    #print(hora)
    if hora >= 0 and hora < 13:
        print("Buenos días son las ")
        os.system("time /T")
    elif hora >= 13 and hora < 18:
        print("Buenas tardes, son las ")
        os.system("time /T")
    else:
        print(" Buenas noches, son las ")
        os.system("time /T")

def par():
    #os.system("cls")
    n=input("Ingrese un número para saber si es par o impar: ")
    if n.isnumeric():
        m=int(n)
    elif m%2==0:
        print("El numero ",m, "es par")
        input("Presione una tecla para continua")
        pausa=5
        time.sleep(pausa)
    else:
        os.system("cls")
        print("El numero ",m, "es par")
        pausa=5
        time.sleep(pausa)
        input("Presione una tecla para continua")
        #return

def promedio():
    prom=[]
    c=0
    for i in range(5):
        n=input(f"Ingrese el número {i+1}: ")
        if n.isnumeric()== True:
            m=int(n)
            prom.append(m)
            c=c+float(m)
            if c>0:
                r=c/5
        else:
            os.system("cls")
            print("Solo se aceptan numeros")
            return
    print("El promedio de ",prom, "es ",r)

def modulo():
    print("Modulo")

def porcentaje():
    print("POrcentaje")

def potencia():
    print("potencia")

opciones={
        0: salir,
        1: saludar,
        2: par,
        3: promedio,
        4: modulo,
        5: porcentaje,
        6: potencia
    }

def choice(op):
    print(opciones)
    func=opciones.get(op, salir)
    return func()

while True:
    print("\n")
    for i in range(len(menu)):
        print([i],menu[i])
    print("\n")
    try:
        op=int(input("Ingrese una opcion del menu: "))
    except:
        os.system("cls")
        print("================================")
        print("Debe ingresar una opcion valida ")
        print("================================")
        print("\n")
        input("Presione una tecla para continuar")
        continue
    choice(op)