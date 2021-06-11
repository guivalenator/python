import os
#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi","Elegir opión de menú favorita", "Cerrar sesión"]
d=0
#i=0
j=7
c=0
s=0
#password=None

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
                inicio(7,1)
            else:
                os.system ("cls") 
                print("Error")
        else:
            os.system ("cls") 
            print("Error")
    else:
        os.system ("cls") 
        print("Error")

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
                            #pass_change()
                            coordenadas()
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

def coordenadas():
    filas=3
    columnas=1
    #coord=[[]*filas for i in range(columnas)]
    coord=[]
    print(coord)
    for i in range(filas):
        coord.append([])
        for j in range(columnas):
            lat=input("Ingrese Latitud: ")
            if (len(lat)>=5 and len(lat)<=7) and lat!="" and lat.isalpha()== False and lat.count(".")==1:
                indice=lat.find(".")
                decimales=lat[indice+1:len(lat)]
                entero=lat[0:indice]
                if len(decimales)==3 and decimales.isnumeric()==True and entero.isnumeric()==True:
                    lat=entero+"."+decimales
                    if float(lat)>= 9.757 and float(lat) <=10.462 and lat != "":
                        coord[i].append(lat)
                        lon=(input("Ingrese Longitud: "))
                        if len(lon)==7 and lon!="" and lon.isalpha()== False and lon.count(".")==1:
                            indice=lat.find(".")
                            decimales=lon[indice+1:len(lon)]
                            entero=lon[0:indice]
                            if len(decimales)==3 and decimales.isnumeric()==True and entero.isnumeric()==True:
                                lon=entero+"."+decimales
                        if float(lon)>=-73.623 and float(lon)<=-72.987:
                            print("entró")
                            coord[i].append(lon)
                        else:
                            print("Error coordenada")
                    else:
                        print("Error coordenada")
                else:
                    print("Error coordenadas")
            else:
                print("Error coordenadas")
    print(coord)

def pass_change():
    global passwd
    print(passwd)
    actual_pass=input("Ingrese la contraseña actual: ")
    if passwd==actual_pass:
        new_pass=input("Ingrese la nueva contraseña: ")
        if new_pass == passwd:
            exit()
        else:
            passwd
            passwd=new_pass
            inicio(7,1)
    else:
        exit()

#login()
coordenadas()