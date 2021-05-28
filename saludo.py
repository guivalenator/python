print("ingrese la hora en punto del dia en formato 24 horas. Ejemplo 15")
hora=00


try :
    hora=int(input("ingrese la hora (00...23): "))
    if hora < 24:
        print(hora)
    #long=hora.len() == 2
    if hora>=0 and hora<12:
        print("Buenos dias")
    elif hora >=12 and hora <=18:
        print("Buenas tardes")
    elif hora >=19 and hora <=23:
        print("Buenas noches")
    else:
        print("Debes Ingresar un numero mayor o igual a cero y menor que 23")
except:
    print("Debes ingresar numeros")