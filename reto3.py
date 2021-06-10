import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
d=0
#i=0
j=7
c=0
s=0

#RF01 Mensaje de Bienvenida
saludo="""
===========================================================

Bienvenido al sistema de Ubicación para zonas públicas WIFI

===========================================================
"""
print(saludo)

def pass_change():
    global passwd
    actual_pass=input("Ingrese la contraseña actual: ")
    if passwd==actual_pass:
        new_pass=input("Ingrese la nueva contraseña: ")
        if new_pass == passwd:
            exit()
        else:
            passwd=new_pass
            inicio(7,1)
    else:
        exit()

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
#Inicio Reto 2                
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

                #RF02 Menu Favoritos
                def favoritos(c):
                    try:
                        inicio(5,0)
                        #RF04 Opciones menu Favoritos
                        k=int(input("Seleccione opción favorita"))
                        if k>0 and k<6 and c<4:
                            c=0
                            l=1
                            l=int(input("Para confirmar por favor responda:Soy un numero impar y despues del 5 me encontraras...la respuesta es: "))
                            if l==7:
                                m=1
                                m=int(input("Para confirmar por favor responda:Soy un numero impar y antes del 7 me encontraras...la respuesta es: "))
                                if m==5:
                                    opciones.insert(0,opciones[k-1])
                                    opciones.pop(k)
                                    os.system("cls")
                                    c=0
                                    inicio(7,1)
                                else:
                                    c=0
                                    os.system("cls")
                                    print("Error")  
                                    inicio(7,1)
                            else:
                                os.system("cls")
                                print("Error")    
                                c=0
                                inicio(7,1)
                        else:
                            c=0
                            os.system("cls")
                            print("Error")
                            inicio(7,1)
                    except:
                        c=0
                        os.system("cls")
                        if l==1:
                            print("Error")
                            inicio(7,1)
                        elif m==1:
                            print("Error")
                            inicio(7,1)
                        else:
                            os.system("cls")
                            print("Error")
                #RF03 Menu Principal
                def menu():
                    try:
                        global s
                        global c
                        s=1
                        op=int(input("Elija una opción"))
                        print("")
                        if op>0 and op<6:
                            c=0
                            os.system("cls")
                            print("Usted ha elegido la opción",op)
                            pass_change()
                        else:
                            #os.system("cls")
                            if op==6:
                                c=0
                                s=0
                                os.system("cls")
                                favoritos(0)
                                os.system("exit")
                            else:
                                #RF05: El programa permite al usuario salir del menú
                                os.system("cls")
                                if op ==7:
                                    print("Hasta pronto")
                                else:
                                    print("Error")
                                    inicio(7,1)
                    except:
                            if s==0:
                                print("Error")
                                exit()
                            else:
                                os.system("cls")
                                print("Error")
                                inicio(7,1)
#Fin Reto 2
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
    

os.system("cls")
inicio(7,1)
