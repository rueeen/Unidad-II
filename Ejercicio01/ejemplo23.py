#Lista vacia
lst = ["Perico los Palotes", "Maria las Petunias"]

#Ciclo infinito
while True:
    print("1. Agregar nombre")
    print("2. Modificar nombre")
    print("3. Mostrar lista")
    print("4. Eliminar nombre")
    print("0. Salir")
    
    op = input('Ingrese su opcion\n')
    
    if op == '1':
        #Agregando elementos a la lista
        nombre = input("Ingrese el nombre a agregar\n")
        lst.append(nombre)
        print("Se agrego un nuevo nombre a la lista")
        
    elif op == '2':
        #modificar un elemnto de la lista
        print(lst)
        i = int(input('Ingrese indice de elemento a modificar\n'))
        nuevo_nombre = input('Ingrese nuevo nombre\n')
        #Para modificar necesitamos
        #indice y nuevo valor
        lst[i] = nuevo_nombre
    
    elif op == '3':
        if len(lst) == 0:
            print("No hay elementos en la lista")
        else:
            #print(lst)
            #recorrer lista e imprimir por separado sus datos
            for i in lst:
                #i representa CADA ELEMENTO de la lista
                print(f'Nombre: {i}')
                print('-------------------------')
        
    elif op == '4':
        #Eliminando nombre de la lista
        #Se necesita el indice del elemento a eliminar
        print(lst)
        i = int(input('Ingrese indice de elemento a modificar\n'))
        del lst[i]
        
    elif op == '0':
        print('Saliendo de programa...')
        break
    
    else:
        print('Opcion no valida')
        
