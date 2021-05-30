#variables
print("Ingrese 2 numeros diferente de 0")
print("primer numero: >>>")
n1=int(input())
print("segundo numero: >>>")
n2=int(input())
n3=3
booleano=False
#validacion de numeros
if n1 !=0 and n2!=0 and n1>0 and n2>0:
    print("1. >> Los numeros igresados son enteros diferentes de 0")
    if n1%2==0 and n2%2==0:
        booleano=True
    #operaciones aritmeticas
    suma=n1+n2
    resta=n1-n2
    division=n1/n2
    mod=n1%n2
    potencia=n1**n3
    residuo=n1//n2
    raiz=n1**0.5
    raiz=n2**0.5
    r1=(7+5*3)
    r2=(-5+(-9))
    r3=-10+8
    r4=(7-3*(5/2)**3)
    r5=(86/2)+150
    r6=(3-5*(45*3))
    r7=55>=55
    r8=100>10000
    r9=80!=80
    r10=4<9
    r11=63<=70
    r12=455==455

    #operaciones de relacion
    print("2. >> La suma de",n1,"y",n2, "Es igual a: ",suma)
    print("3. >> La resta de",n1,"y",n2, "Es igual a: ",resta)
    print("4. >> ",n1,"dividido",n2, "Es igual a: ",division)
    print("5. >> ",n1,"modulo",n2, "Es igual a: ",mod)
    print("6. >> ",n1,"elevado a la",n3, "Es igual a: ",potencia)
    print("8. >> El residuo de", n1,"divido",n2, "Es igual a: ",residuo)
    print("9. >> La raiz cuadra de", n1, "Es : ",raiz)
    if n1>n2:
        print("10. >> ",n1," es mayor que ",n2)
    else:
        if n1<n2:
            print("11. >> ",n1," es menor que ",n2)
        else:
            print("11. >> ",n1," es igual ",n2)
    print("12.>> (7+5*3)=",r1)
    print("13. >> (-5+(-9))=",r2)
    print("14. >> -10+8==",r3)
    print("15. >> (7-3*(5/2)**3)",r4)
    print("16. >> -(86/2)+150=",r5)
    print("17. >> (3-5*(45*3))=",r6)
    print("18. >> La variable booleana es: ",booleano)
    print("19. >> 55>=55",r7)
    print("20. >> 100>10000",r8)
    print("21 >> 80!=80",r9)
    print("22. >> 4<9",r10)
    print("23. >> 63<=70",r11)
    print("24. >> 455==455",r12)

else:
    print("Los numeros ingresados no son validos")
    
