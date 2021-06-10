import os
#Lista con las opciones del menu
menu=["Salir","Saludar","Es Par","Promedio","Modulo","Porcentaje","Potencia"]

#Ciclo para recorrer la lista y generar la ocpiones del menu
print("====================")
print("Menu de opciones")
print("====================\n")

def salir():
    exit("Bye")

def saludar():
    print("Hola")

def par():
    print("par")

def promedio():
    print("promedio")

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
    func=opciones.get(op, salir)
    return func()

while True:
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