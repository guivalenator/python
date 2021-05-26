opciones="""
    =====================
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Potencia
    6. Salida
    =====================
    """

def default():
    return "Opcion Invalida"


def switch(case,a,b):
    switcher={
        1: opcion1(a,b),
        2: opcion2(a,b),
        3: opcion3(a,b),
        4: opcion4(a,b),
        5: opcion5(a,b),
        6: "Salida"
    }
    return switcher.get(op,default())


def opcion1(a,b):
    a1=str(a)
    b1=str(b)
    s=a+b
    r1=str(s)
    f=a1+"+"+b1+"="+r1
    return f

def opcion2(a,b):
    s=a-b
    return s

def opcion3(a,b):
    s=a*b
    return s

def opcion4(a,b):
    s=a/b
    return s

def opcion5(a,b):
    s=a**b
    return s

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))

print(opciones)
op=int(input("Elija la opcion: "))
print(switch(op,a,b))
