ent=input("Ingrese la temperatura")

try:
    fahr=float(ent)
    cel=(fahr-32)*5/9
    print(cel)
except:
    print("POr favor intruduzcaun numero valido")

try:

except NameError: #valida error en variable
    print("Mensaje")

except ValueError:# valida si el valor es numerico
    print("Mensaje")
