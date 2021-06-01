#creación del menú
lista=[]
def menu():
    print("Menú")
    print("1.Agregar datos a la lista")
    print("2. Eliminar un dato de una lista dado el dato")
    print("3. Eliminar un dato dada la posición")
    print("4. Agregar un dato en una posición deseada.")
    print("5. Cantidad de veces que aparece un elemento dado en la lista")
    print("6. Ordenar la lista de menor a mayor")
    print("7. salir")

#agregar datos a la lista
def agregarlista(lista):
   dato1=int(input("ingrese el dato a ingresar"))
   lista.append(dato1)
   return(lista)

#eliminar dato dado ese dato
def eliminar(lista):
    dato2=int(input("Ingrese el dato a eliminar"))
    p=lista.index(dato2)
    if p==-1:
        print("dato no encontrado")
    else:
        del lista[p]
    return lista

#manejo de las opciones
def switch(opcion,lista):
    diccionario={
        1: agregarlista(lista),
        2: eliminar(lista),
        3: "Eliminar un dato dada la posición\n",
        4:"Agregar un dato en una posición deseada.\n",
        5:"Cantidad de veces que aparece un elemento dado en la lista",
        6:"Ordenar la lista de menor a mayor",
        7:"salir",
    }
    return diccionario.get(opcion,"Opción invalida") 

  

#Proceso de selección de opciones y operaciones
while True:
    menu()
    try:
        op=int(input("Ingrese la opción deseada"))
        print(switch(op,lista))
        if(op==7):
         break
    except ValueError:
        print("Error, solo debe ingresar valores numericos")