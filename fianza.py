'''Una compañía de seguros está abriendo un depto. de finanzas y estableció un programa 
para captar clientes, que consiste en lo siguiente: Si el monto por el que se efectúa la fianza 
es menor que $50 000 la cuota a pagar será por el 3% del monto, y si el monto es mayor o 
igual que $50 000 la cuota a pagar será el 2% del monto. La afianzadora desea determinar 
cuál será la cuota que debe pagar un cliente'''
from typing import ChainMap


monto=input("Ingrese el valor del monto")

try:
    cap=int(monto)
    if cap < 50000:
        print("cuota a pagar: ", cap*0.03)
    else:
        print("cuota a pagar: ",cap*0.02)
except NameError:
    print("Error en variable")
except ValueError:
    print("Ingrese un numero valido")

