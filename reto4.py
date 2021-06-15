import os
from typing import Dict
import ast
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]

#Variables globales
llenado=0
c=0

#Declaracion y llenao con ceros de la matriz (lista de listas)
#coord=[['1.740', '-75.950'], ['1.880', '-75.950'], ['1.940', '-75.950']]
coord=[]
for i in range(3):
    coord.append([0]*2)

#Funcion de login
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
    global passwd
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
                print("\n")
                menu()
            else:
                os.system ("cls") 
                print("Error")
        else:
            os.system ("cls") 
            print("Error")
    else:
        os.system ("cls") 
        print("Error")

#Funcion para el menu principal
def menu(z=7):
    print("=============================")
    print("        MENÚ PRINCIPAL       ")
    print("=============================")
    Dict={}
    for i in range(len(opciones)):
        Dict[i+1]=(opciones[i])[0:5].lower()
    
    while True:
        for i in range(z):
            print(i+1,opciones[i])

        print("\n")
        op=int(input("Elija una opción:  "))
        func=Dict.get(op, cerra)
        func=eval(func)
        return func()

#Funcion para el cambio de contraseña
def cambi():
    global passwd
    actual_pass=input("Ingrese la contraseña actual: ")
    if passwd==actual_pass:
        new_pass=input("Ingrese la nueva contraseña: ")
        if new_pass == passwd:
            print("No puede asignar la misma contraseña:")
            print("Error")
            exit()
        else:
            passwd
            passwd=new_pass
            menu()
    else:
        print("Error")
        exit()

#Funcion para verificar y mostrar coordenas ya ingresadas
def ingre():
    os.system("cls")
    op=None
    if llenado==1:
        print("coordenada [latitud,longitud] 1 :",coord[0])
        print("coordenada [latitud,longitud] 2 :",coord[1])
        print("coordenada [latitud,longitud] 3 :",coord[2])
        sur=[]
        oriente=[]
        for i in range(len(coord)):
            for j in range(0,len(coord)-1,2):
                sur.append(coord[i][j])

        for i in range(len(coord)):
            for j in range(1,len(coord)-1,2):
                oriente.append(coord[i][j])
        print("\n")        
        print(f"La coordenada {sur.index(min(sur))+1} está ubicada más al sur")
        print(f"La coordenada {oriente.index(max(oriente))+1} está ubicada más al oriente")
        print("\n")
        op=input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú: ")
        if op =="1":
            update_coord(1,1,0)
        elif op =="2":
            update_coord(2,1,1)
        elif op=="3":
            update_coord(3,1,2)
        elif op=="0":
            os.system("cls")
            menu()
        else:
            print("Error actualización")
            os.system("exit")
    else:
        print("No tiene coordenadas frecuentes asigandas")
        print("Ingrese las coordenadas del trabajo, la casa y el parque")
        update_coord()

#Funcion para ingresar y actualizar coordenadas
def update_coord(fil=3,col=1,ini=0):
    global llenado
    llenado=0
    for i in range(ini,fil):
        for j in range(col):
            lat=input("Ingrese Latitud: ")
            if (len(lat)>=5 and len(lat)<=7) and lat!="" and lat.isalpha()== False and lat.count(".")==1:
                indice=lat.find(".")
                decimales=lat[indice+1:len(lat)]
                entero=lat[0:indice]
                if len(decimales)==3 and decimales.isnumeric()==True and entero.isnumeric()==True:
                    lat=entero+"."+decimales
                    if float(lat)>= 1.740 and float(lat) <=1.998 and lat != "":
                        #Ingreso y validacion de la longitud
                        lon=input("Ingrese Longitud: ")
                        if len(lon)==7 and lon!="" and lon.isalpha()== False and lon.count(".")==1:
                            indice=lon.find(".")#Ubica la posicion del punto en la cadena
                            decimales=lon[indice+1:len(lon)]#Extrae los caracteres despues del punto
                            entero=lon[0:indice]# Extrae la parte numerica a la izquierda del punto 
                            if len(decimales)==3 and decimales.isnumeric()==True:# valida la cantidad de decimales, que la cadena sea numerica
                                lon=entero+"."+decimales#concatena parte entera y decimal
                                if float(lon)>= -75.950 and float(lon)<=-75.689:
                                    coord[i][j]=lat
                                    coord[i][j+1]=lon
                                else:
                                    print("Error coordenada")
                                    exit()
                        else:
                            print("Error coordenada")
                            exit()
                    else:
                        print("Error coordenada")
                        exit()
                else:
                    print("Error coordenada")
                    exit()
            else:
                print("Error coordenada")
                global c
                c=4
                exit()               
    llenado=1
    menu()

#Funcion ubicacion zona wifi
def ubica():
    print("usted ha elegido la opción: ",opciones.index("Ubica zona wifi más cercana")+1)

#Funcion guardar ubicacion
def guard():
    print("usted ha elegido la opción: ",opciones.index("Guardar archivo con ubicación cercana")+1)

#Funcion actualizar
def actua():
    print("usted ha elegido la opción: ",opciones.index("Actualizar registros de zonas wifi")+1)

#Funcion de Favoritos
def elegi(c=0):
    os.system("cls")
    print("=================================")
    print("Parametrizar el menú de favoritos")
    print("=================================")
    print("\n")
    try:
        for i in range(5):
            print(i+1,opciones[i])
        #RF04 Opciones menu Favoritos
        print("\n")
        k=int(input("Seleccione opción favorita: "))
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
                    menu()
                else:
                    c=0
                    os.system("cls")
                    print("Error")  
                    menu()
            else:
                os.system("cls")
                print("Error")    
                c=0
                menu()
        else:
            c=0
            os.system("cls")
            print("Error")
            menu()
    except: 
        c=0
        os.system("cls")
        if l==1:
            print("Error")
            menu()
        elif m==1:
            print("Error")
            menu()
        else:
            os.system("cls")
            print("Error")

#Funcion para salir del programa
def cerra():
    print("Hasta pronto")
    exit()

#Inicio del programa
login()