import os

a=open("zona_wifi.txt","r")
archivo_externo=open("zona_wifi.txt","r")
contenido=archivo_externo.readlines()#.splitlines()
print(contenido)
l = []
for line in archivo_externo:
    l.append(line.rstrip().split(','))
print(l)
archivo_externo.close()

l=[]

f = open("zona_wifi.txt", "r")
for i in range(f):
    l.append([])
    while(True):
        linea = f.readline().strip("\n")
        i=i+1
        print(linea)
        if not linea:
            break

f.close()
print(l)
#prueba=[]
'''for i in contenido:
    prueba.append([])
    for j in contenido:
        linea=archivo_externo.readline().strip("\n")
        prueba[j].append(linea)'''
'''print("archivo_externo")
print(contenido)
print(prueba)
archivo_externo.close()'''
