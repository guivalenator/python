import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
contactor=True
j=7

def inicio(j):
    os.system("cls")
    while contactor:
        #print(i)
        for i in range(j):
            print(i+1,".",opciones[i])
        print("")
        break
inicio(j)
try:
    op=int(input("Elija una opción: "))
    os.system("cls")
    if op>0 and op<6:
        print("Proceso X")
        #inicio(j=7)
    elif op==6:
        os.system("cls")
        inicio(j=4)
        kere=int(input("Seleccione opción favorita:"))
        k=kere
        if k <= 5:
            opciones.insert(0,opciones[k-1])
            opciones.pop(k)
            #os.system("cls")
            inicio(i=7)
        else:
            print("Que vaina")
    elif op ==7:
        contactor=True
        print("Gracias por utilizar esta APP")
    else:
        print("opcion invalida")
except:
    print("opcion invalida. Ingrese un numero")
    