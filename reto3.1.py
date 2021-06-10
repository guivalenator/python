import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
d=0
#i=0
j=7
c=0
s=0

def login():
    os.system("cls")
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
            t1=675
            t2=int((6+1)-(5%5))
            print(t1, "+", t2,"=")
            r=(input())
            if r.isnumeric and int(r)==t1+t2:
                # RF04 Confirmacion de ingreso al sistema
                os.system ("cls") 
                print("Sesión iniciada")
            else:
                os.system ("cls") 
                print("Error")
        else:
            os.system ("cls") 
            print("Error")
    else:
        os.system ("cls") 
        print("Error")

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

login()