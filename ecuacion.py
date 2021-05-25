#Definicion de variables
a=2
b=9
c=10
#Formula a usar
print("ecuacion a despejar")
print("          _________")
print("      -b±V b²-4ac")
print("X=--------------------")
print("          2a        ")
#Calculo

x1=-b+(((b**2)-(4*a*c))**0.5)/(2*a)
x2=-b-(((b**2)-(4*a*c))**0.5)/(2*a)
x3=-(((b**2)-(4*a*c))**0.5)

#Salida por pantalla
print(x1)
print(x2)
print(x3)
