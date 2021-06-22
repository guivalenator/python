import os
from typing import Dict
import ast
import math
from math import *

#RF01 Menu de Opciones
opciones=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubica zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opión de menú favorita", "Cerrar sesión"]

#Variables globales
llenado=0
ubi_actual=0
informacion=dict()
passwd=None
c=0

#Declaracion y llenado con ceros de la matriz (lista de listas) para almacenar mis ubicaciones
coord=[]
for i in range(3):
    coord.append([0]*2)
#coord=[['1.740', '-75.910'], ['1.880', '-75.950'], ['1.940', '-75.689']]

#Declaracion y llenado con ceros de la matriz (lista de listas) para importar coordenadas de zonas wifi
zona_wifi=[]
for i in range(4):
    zona_wifi.append([0]*3)
zona_wifi=[['1.811', '-75.820', '58'], ['1.919', '-75.843', '1290'], ['1.875', '-75.877', '110'], ['1.938', '-75.764', '114']]


#Funcion de login para ingresar a la aplicaion
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
    #passwd_ing=None

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
    #Se genera el menu principal desde una lista de valores
    for i in range(len(opciones)):
        Dict[i+1]=(opciones[i])[0:5].lower()#Se crea el valor del indice y se capturan los 5 primeros caracteres de la lista para convertilos en el nombre de la funcion
    
    while True:#Recorre la lista y muestra el nombre completo de la opcion del menu
        for i in range(z):
            print(i+1,opciones[i])

        print("\n")
        op=int(input("Elija una opción:  "))
        func=Dict.get(op, cerra)#Se obtiene el nombre de la funcion a ejecutar
        func=eval(func)#el metodo eval() toma el string de la variable funcion y lo convierte en un dato crudo(diferente a string)
        return func()

#Funcion para el cambio de contraseña
def cambi():
    global passwd
    actual_pass=input("Ingrese la contraseña actual: ")
    if passwd==actual_pass:
        new_pass=input("Ingrese la nueva contraseña: ")
        if new_pass == passwd:
            print("No puede asignar la misma contraseña: ")
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
    if llenado==1:#Se valida con este campo que ya se hayan ingresado las coordendas comunes del usuario
        for i in range(len(coord)):
            print(f"coordenada [latitud,longitud] {int(i)+1} : {coord[i]}")

        sur=[]
        oriente=[]
        #Se crean listas para almacenar aparte las latitudes y longitudes
        for i in range(len(coord)):
            for j in range(0,len(coord)-1,2):
                sur.append(coord[i][j])

        for i in range(len(coord)):
            for j in range(1,len(coord)-1,2):
                oriente.append(coord[i][j])
    
        print("\n")        
        print(f"La coordenada {sur.index(min(sur))+1} está ubicada más al sur")
        print(f"La coordenada {oriente.index(min(oriente))+1} está ubicada más al oriente")
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
def update_coord(fil=3,col=1,ini=0,wifi=0):
    global llenado
    llenado=0
    for i in range(ini,fil):
        for j in range(col):#La iteracione de este ciclo es solo una ya que se ingresan de una vez los datos en su respectiva columna 
            lat=input(f"Ingrese latitud de la coordenada {i+1}: ")
            if (len(lat)>=5 and len(lat)<=7) and lat!="" and lat.isalpha()== False and lat.count(".")==1:#Se valida que la opcion ingresada este en el rango correcto, que no se un espacio en blanco que no se alfabetico y que contenga el caracter punto(.)
                indice=lat.find(".")#Se obtiene el indice(ubicacion)del caracter punto(.)
                decimales=lat[indice+1:len(lat)]#Se cuenta el numero de caracteres despues del punto
                entero=lat[0:indice]#Se convierten los numeros antes del punto en entero
                if len(decimales)==3 and decimales.isnumeric()==True and entero.isnumeric()==True:#Se valida que el valor ingresado tenga 3 decimales y tenga la parte entera
                    lat=entero+"."+decimales #Se almacena el string en formato entero.decimal
                    if float(lat)>= 1.740 and float(lat) <=1.998 and lat != "":
                        #Ingreso y validacion de la longitud
                        lon=input(f"Ingrese longitud de la coordenada {i+1}: ")
                        if len(lon)==7 and lon!="" and lon.isalpha()== False and lon.count(".")==1:
                            indice=lon.find(".")#Ubica la posicion del punto en la cadena
                            decimales=lon[indice+1:len(lon)]#Extrae los caracteres despues del punto
                            entero=lon[0:indice]# Extrae la parte numerica a la izquierda del punto 
                            if len(decimales)==3 and decimales.isnumeric()==True:# valida la cantidad de decimales, que la cadena sea numerica
                                lon=entero+"."+decimales#concatena parte entera y decimal
                                if float(lon)>= -75.950 and float(lon)<=-75.689: # Se validan los rangos de la longitud
                                    if wifi==0:
                                        coord[i][j]=lat
                                        coord[i][j+1]=lon
                                    else:
                                        print(zona_wifi)
                                        conexiones=input(f"Ingrese usuarios conectados en la coordenada {i+1}: ")
                                        print(i,j)
                                        zona_wifi[i][j]=lat
                                        print(i,j+1)
                                        zona_wifi[i][j+1]=lon
                                        print(i,j+2)
                                        zona_wifi[i][j+2]=conexiones
                                        print(zona_wifi)

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
    #global puntos
    if llenado==0:
        print("Error sin registro de coordenadas")
        exit()
    else:
        os.system("cls")
        for i in range(len(coord)): #muestra coordenadas ingresadas por el usuario
            print(f"coordenada [latitud,longitud] {int(i)+1} : {coord[i]}")
        print("\n")

    op=input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ")
    if op >="1" and op<="3":
        global ubi_actual
        ubi_actual=1
        op=int(op)
        for i in range(op-1,op): #obtiene coordenada segun la opcion seleccionada
            lat1=float(coord[op-1][0])
            lon1=float(coord[op-1][1])
            informacion['actual']=[coord[op-1][0],coord[op-1][1]] #Ingresa posicion actual al diccionario
        cercana(lat1,lon1,ubi=op) #Funcion ára calcular distancia de la ubicacion selecionada
        ordenada=sorted(puntos, key=lambda x: x[1], reverse=False) #Ordena coordendas en orden ascendente segun segunda columna de la lista puntos
        #os.system("cls")
        print("Zonas wifi cercanas con menos usuarios")
        print("\n")
        for i in range(2):
            for j in range(1):
                print(f"La zona wifi {(puntos[i][j])+1}: ubicada en [\'{zona_wifi[(ordenada[i][j])][j]}\',\'{zona_wifi[(ordenada[i][j])][j+1]}\'] a {ordenada[i][j+1]*1000:.0f} metros , tiene en promedio {zona_wifi[(ordenada[i][j])][j+2]} usuarios")
        print("\n")
        op=input("Elija 1 o 2 para recibir indicaciones de llegada: ")
        if op >="1" and op <="2" :

            op=int(op)-1
            lat_wifi_1=zona_wifi[(ordenada[op][0])][0]
            lon_wifi_1=zona_wifi[(ordenada[op][0])][1]
            dist=ordenada[op][1]
            informacion['zonawifi1']=[lat_wifi_1,lon_wifi_1,zona_wifi[(ordenada[op][0])][2]] #almacena zona wifi seleccionada en el diccionario informacion
            direccion(lat1,lon1,lat_wifi_1,lon_wifi_1,dist) #Funcion para calcular la direccion y tiempos de llegada
        else:
            print("Error zona wifi")
            os.system("exit")
        
    else:
        print("Error ubicación")
        os.system("exit")

def cercana(lat1, lon1, ubi): #Funcion para calcular la distancia entre coordenadas recibe argumentos de la ubicacion actual
    c=math.pi/180 #para convertir grados decimales a radianes
    r=6372.795477598 #Diametro de la tierra
    global puntos
    puntos=[]
    for i in range(4):
        puntos.append([])
        for j in range(1):
            lat2=float(zona_wifi[i][j])
            lon2=float(zona_wifi[i][j+1])
            Alat=lat1-lat2
            Alon=lon1-lon2       
            dist = 2*r*asin(sqrt(sin(c*(lat2-lat1)/2)**2 + cos(c*lat1)*cos(c*lat2)*sin(c*(lon2-lon1)/2)**2)) #Formula para hallar la distancia entre coordenas
            #dist=2*r*math.asin(math.sqrt(math.pow(math.sin(c*(Alat/2)),2))+(math.cos(c*lat1)*math.cos(c*lat2)*(math.pow(math.sin(c*(Alon/2)),2))))
            puntos[i].append(i+0) #añade indice de la ubicacion seleccionada
            puntos[i].append(dist) #Añade distancia entre las coordenadas de ubicacion actual y las zonas wifi
            print("\n")
    return puntos

def direccion(lat1,lon1,lat_wifi_1,lon_wifi_1,dist): #Muestra la direccion a seguir y los promedios de tiempo para llegar a la ubicaion
    print("\n") 
    if lat1>float(lat_wifi_1) and lon1>float(lon_wifi_1): 
        print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el oriente")
    elif lat1 > float(lat_wifi_1) and lon1<float(lon_wifi_1):
        print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
    elif lat1 < float(lat_wifi_1) and lon1>float(lon_wifi_1):
        print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
    else:
        print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")

    tiempo_moto=(dist*1000)/19.44 #calcula distancia promedio en moto
    tiempo_a_pie=(dist*1000)/0.483 #calcula distancia promedio caminando
    informacion['recorrido']=[round(dist*1000,2),'moto',round(tiempo_moto,1)] #Añade clave recorrido y sus valores
    
    

    print("\n")
    print(f"Tiempo promedio en moto {tiempo_moto:.0f}")
    print(f"Tiempo promedio a pie {tiempo_a_pie:.0f}")
    op=input("Presione 0 para salir: ")
    if op=="0":
        menu()
    else:
        print("Error")
        exit()

#Funcion guardar ubicacion
def guard():
    if llenado==0 and ubi_actual==0: #Se valida llenado de coordenadas habituales del usuario y seleccion de la ubicacion actual
        print("Error de alistamiento")
        exit()
    else:
        print(informacion)
        op=input("¿Está de acuerdo con la informacion a exportar? Presione 1 para confirmar, 0 para regresar al menú principal: ")
        if op =="1":
            print("Exportando archivo")
            with open('archivo.txt', 'w') as archivo: # Se abre archivo externo en modo escritura
                archivo.write(str(informacion)) #Escribe informacion del diccionario en archivo externo
            with open("archivo.txt", "r") as fichero: #Abre archivo externo en modo solo lectura
                exit()
        elif op=="0":
            menu()
        else:
            print("Error")

        os.system("cls")

#Funcion actualizar
def actua():
    global zona_wifi
    lista=[]
    matriz=[]
    i=0
    f = open("zona_wifi.txt", "r")
    lineas=f.readline()
    for elemento in f: #Recorre elementos del archivo externo
        matriz.append([])
        lista=elemento.split(",") #Almacena elementos segun separacion coma(,) en una lista
        matriz[i].append(float(lista[0]))
        matriz[i].append(float(lista[1]))
        matriz[i].append(float(lista[2]))
        i+=1
    
    zona_wifi.clear()#Limpia matriz 
    zona_wifi=matriz #copia una nueva matri
    f.close()
    print("Actualizando coordenadas...")
    op=input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
    if op=="0":
        menu()
    else:
        print("Error")
        exit()
    
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