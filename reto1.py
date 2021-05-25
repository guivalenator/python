import os
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
  