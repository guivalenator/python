import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
d=0
i=0
j=7
#k=None
#l=None
#m=0
c=0

def inicio(j,d):
    global c
    while c<3:
        for i in range(j):
            print(i+1,".",opciones[i])
        print("")
        if d==1:
            c+=1
            menu()
        else:
            h=0
        break

def favoritos(c):
    try:
        #while c < 3 :
            #print(c)
            inicio(5,0)
            k=int(input("Seleccione opción favorita"))
            if k>0 and k<6 and c<4:
                c=0
                l=0
                l=int(input("Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                if l==9:
                    m=0
                    m=int(input("Para confirmar por favor responda:Soy un numero impar y despues del 5 me encontraras...la respuesta es: "))
                    if m==7:
                        opciones.insert(0,opciones[k-1])
                        opciones.pop(k)
                        os.system("cls")
                        c=0
                        inicio(7,1)
                    else:
                        c=0
                        inicio(7,1)
                else:
                    os.system("cls")
                    c=0
                    inicio(7,1)
            else:
                c=4
                os.system("cls")
                print("Error")
            #break
    except:
        c=0
        os.system("cls")
        if l==1:
           inicio(7,1)
        elif m==1:
           inicio(7,1)
        else:
            os.system("cls")
            print("Error")

def menu():
    try:
        op=int(input("Elija una opción"))
        os.system("cls")
        if op>0 and op<6:
            print("Usted ha elejido la opción ",op)
            op=0
        else:
            #os.system("cls")
            if op==6:
                global c
                c=0
                favoritos(0)
            else:
                os.system("cls")
                if op ==7:
                    print("Hasta pronto")
                else:
                    input("...0")
                    print("Error44")
                    inicio(7,1)
    except:
        os.system("cls")
        print("Error")
        inicio(7,1)


os.system("cls")
inicio(7,1)
