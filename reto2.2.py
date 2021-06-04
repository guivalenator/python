import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
d=0
i=0
j=7

c=0
#RF01 Mensaje de Bienvenida
saludo="""
===========================================================

Bienvenido al sistema de Ubicación para zonas públicas WIFI

===========================================================
"""
print(saludo)

#RF02 Nombre de usuario y contraseña
usuario="51675"
passwd="57615"

user_ing=input("Ingrese su usuario: ")
passwd_ing=None

if user_ing==usuario:
    passwd_ing=input("Ingrese contaseña: ")
    if   passwd_ing==passwd:
        #RF03 Resolucion del captcha 
        print("Calcule y digite el resultado de la siguiente operacion:")
        r=None
        t1=675
        t2=int((6+1)-(5%5))

        print(t1, "+", t2,"=")
        #r=input()
        try:
            r=int(input())
            #r=int(r)
            if r==t1+t2:
                # RF04 Confirmacion de ingreso al sistema
                os.system ("cls") 
                print("Sesión iniciada")
                def inicio(j,d):
                    global c
                    while c<4:
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
                                    print("Error")
                                    inicio(7,1)
                    except:
                        os.system("cls")
                        print("Error")
                        inicio(7,1)


                os.system("cls")
                inicio(7,1)

            else:
                os.system ("cls") 
                print("Error")
        except:
                os.system ("cls") 
                print("Error")
    else:
        os.system ("cls")
        print("Error")
else:
    os.system ("cls") 
    print("Error")
  