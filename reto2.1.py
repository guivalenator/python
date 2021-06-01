import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
c=0
d=0
i=0
j=7
k=None
l=None
m=0

def inicio(j,d):
    #os.system("cls")
    while True:
        #print(i)
        for i in range(j):
            print(i+1,".",opciones[i])
        print("")
        break
    if d==1:
        menu()
    else:
        c=0


def favoritos(c):
    k=0
    l=0
    m=0
    try:
        while c < 3 :
            inicio(5,0)
            k=int(input("Seleccione opción favorita"))
            if k>0 and k<6 and c<4:
                l=int(input("Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                if l==9:
                    l=1
                    m=int(input("Para confirmar por favor responda:Soy un numero impar y despues del 5 me encontraras...la respuesta es: "))
                    if m==7:
                        m=1
                        opciones.insert(0,opciones[k-1])
                        opciones.pop(k)
                        os.system("cls")
                        inicio(7,0)
                        c=4
                    else:
                        c=4
                        inicio(7)
                else:
                    c=4
                    inicio(7)
            else:
                c=4
                os.system("cls")
                print("Errorote")
    except:
        if l==1:
            inicio(7,1)
        elif m==1:
            inicio(7,1)
        else: 
            input("Error")
            #inicio(7,1)

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
                favoritos(0)
            else:
                os.system("cls")
                if op ==7:
                    print("Hasta pronto")
                else:
                    print("Error numero invalido")         
    except:
        print("Error")

#os.system("cls")
inicio(7,1)

