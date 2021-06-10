print("=======================")
print("      \"Calculadora\" ")
print("=======================")

print(" _____________________")
print("|  _________________  |")
print("| | JO           0. | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
print("\n")



# Ingreso y conversion de numeros
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
op=0
print("\n")

#Lista con las opciones del menu
menu=("1. Suma","2. Resta","3. Multiplicación","4. División","5. Potenciación")

#Ciclo que recorre la lista y muesta las opciones del menu
for i in range(len(menu)):
    print(menu[i])

print("\n")

#Condicional con las opciones a ejecutar
op=input("Seleccione la opcion de la operacion a realizar: ")

if op =="1":
    print("La suma de", a ,"+", b, "es: ",a+b)
elif op =="2":
    print("La resta de", a ,"-", b, "es: ",a-b)
elif op =="3":
    print("La multiplicacion de", a ,"x", b, "es: ",a*b)
elif op =="4":
    print("La division de", a ,"entre", b, "es: ",a/b)
elif op =="5":
    print("La potencia de", a ,"a la", b, "es: ",a**b)
else:
    exit()


#Calculo y proceso de salida del calculo de los datos ingresados
'''print("La suma de", a ,"+", b, "es: ",a+b)

print("La resta de", a ,"-", b, "es: ",a-b)

print("La multiplicacion de", a ,"x", b, "es: ",a*b)

print("La division de", a ,"entre", b, "es: ",a/b)

print("La potencia de", a ,"a la", b, "es: ",a**b)'''