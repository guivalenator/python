#Definicion de variables
a=2
b=9
c=10
#Formula a usar
print("ecuacion a despejar")
print("=======================")
print("          _________")
print("      -b±V b²-4ac")
print("X=--------------------")
print("          2a        ")
print("=======================")
print("Valores dados")
print("=======================")
print("Valor fijo de a: ",a)
print("Valor fijo de a: ",b)
print("Valor fijo de a: ",c)
print("====================")

#Calculo
print("Ingrese los numeros a operar, diferentes de cero")
a1=int(input("Ingrese el valor de a: "))
b1=int(input("Ingrese el valor de b: "))
c1=int(input("Ingrese el valor de c: "))

x1=-b+(((b**2)-(4*a*c))**0.5)/(2*a)
x2=-b-(((b**2)-(4*a*c))**0.5)/(2*a)

y1=-b1+(((b1**2)-(4*a1*c1))**0.5)/(2*a1)
y2=-b1-(((b1**2)-(4*a1*c1))**0.5)/(2*a1)


#Salida por pantalla
print("El resultado de x1 es :",x1)
print("El resultado de x2 es :",x2)

print("El resultado de y1 es :",y1)
print("El resultado de x1 es :",y2)
