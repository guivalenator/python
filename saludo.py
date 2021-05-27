print("ingrese la hora del dia en formato 24 horas. Pimero los minutos y luego los minutos. Ejemplo Hora: 13  Minutos")
hora=00


try :
    hora=int(input("ingrese la hora (00...23): "))<24
    print(hora)
    hora.len() ==2
    minutos=input("ingrese minutos (00...59):")
    int(minutos)
    minutos.len() ==2

    if hora>=0 and hora<12:
        print("Buenos dias")
    elif hora >=12 and hora <=18:
        print("Buenas tardes")
    else:
        print("Buenas noches")
except:
    print("Formato de Hora incorrexto")