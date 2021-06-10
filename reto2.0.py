import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
contactor=True
c=0
i=0
j=7
<<<<<<< HEAD:reto2.1.py

c=0

def inicio(j,d):
    global c
    while c<4:
=======
k=None
l=None
m=0

def inicio(j):
    #os.system("cls")
    while contactor:
        #print(i)
>>>>>>> 78d9fc6ea288ce64ef62a746ec8c0fa6011ed184:reto2.0.py
        for i in range(j):
            print(i+1,".",opciones[i])
        print("")
        break
    #menu()

def favoritos(c):
    k=0
    l=0
    m=0
    try:
        while c < 3 :
            inicio(j=5)
            k=int(input("Seleccione opción favorita"))
            if k>0 and k<6 and c<4:
                l=int(input("Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "))
                if l==9:
                    m=int(input("Para confirmar por favor responda:Soy un numero impar y despues del 5 me encontraras...la respuesta es: "))
                    if m==7:
                        opciones.insert(0,opciones[k-1])
                        opciones.pop(k)
                        os.system("cls")
                        inicio(j=7)
                        input(".....")
                        c=4
            else:
                c=0
    except:
        os.system("cls")
<<<<<<< HEAD:reto2.1.py
        if l==1:
            inicio(7,1)
        elif m==1:
            inicio(7,1)
        else:
            os.system("cls")
            print("Error")
=======
        inicio(j=7)
>>>>>>> 78d9fc6ea288ce64ef62a746ec8c0fa6011ed184:reto2.0.py

def menu():
    try:
        #inicio()
        op=int(input("Elija una opción"))
        os.system("cls")
        #k=0
        if op>0 and op<6:
            print("Usted ha elejido la opción ",op)
            op=0
        else:
            os.system("cls")
        if op==6:
            op=0
            favoritos(0)
            #c=0
            #os.system("cls")
<<<<<<< HEAD:reto2.1.py
            if op==6:
                global c
                c=0
                favoritos(0)
            else:
                os.system("cls")
                if op ==7:
                    print("Hasta pronto")
                else:
                    print("Error")
                    inicio(7,1)
=======
            #inicio(j=4)
            #k=int(input("Seleccione opción favorita:"))
        else:
            os.system("cls")
        if op ==7:
            op=0
            contactor=True
            print("Hasta pronto")
        else:
            os.system("cls")
>>>>>>> 78d9fc6ea288ce64ef62a746ec8c0fa6011ed184:reto2.0.py
    except:
        print("Error")

os.system("cls")
inicio(j)
menu()