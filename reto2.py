import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
contactor=True
c=0
i=0
j=7
k=None
l=None
m=0

def inicio(j):
    os.system("cls")
    while contactor:
        #print(i)
        for i in range(j):
            print(i+1,".",opciones[i])
        print("")
        break
    menu()

def favoritos():
    m=0
    try:
        inicio(j=4)
        k=int(input("Seleccione opción favorita pues:"))<5
        if k>0 and k<5 and c<4:
            opciones.insert(0,opciones[k-1])
            opciones.pop(k)
            os.system("cls")
            l=int(input("Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
            print(l)
            if l==9:
                m=int(input("Para confirmar por favor responda:Soy un numero impar y despues del 5 me encontraras...la respuesta es: "))
            elif m==7:
                inicio(j=7)
                print("")
                print("Elija una opción")
            else:
                    print("Error")
            inicio(j=7)
        else:
            print("POr aca si es")
            c=c+1
            favoritos()
    except:
        c=c+1
        print("Error favoritos")
        favoritos()


def menu():
    try:
        op=int(input("Elija una opción: "))
        os.system("cls")
        #k=0
        if op>0 and op<6:
            print("Proceso X")
            #inicio(j=7)
        elif op==6:
            favoritos()
            #c=0
            #os.system("cls")
            #inicio(j=4)
            #k=int(input("Seleccione opción favorita:"))
        elif op ==7:
            contactor=True
            print("Gracias por utilizar esta APP")
        else:
            print("opcion invalida")
    except:
        print("opcion invalida. Ingrese un numero")

inicio(j)
