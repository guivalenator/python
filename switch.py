menu="""
1- SUMAR
2- RESTAR
3- MULTIPLICAR
"""
print(menu)
op=int(input("Faor digite la opcion deseada"))
a=3
b=4
if op==1:
    s=a+b
    print("Suma=",s)
elif op==2:
    r=a-b
    print("Resta=",r)
elif op==3:
    m=a*b
    print("Multiplicaion=",m)
elif op==4:
    print("Culminaron las operaciones")
else:
    print("opcion incorrecta")



