#Funciones con RETORNO

#print es una funcion SIN RETORNO

#resultado = print('Hola mundo')
#print(resultado) #Imprime None

#None es la ausencia de valor

#input es una funcion CON RETORNO
#resultado = input("Hola mundo\n")
#print(resultado)

def suma(a, b):
    print(a+b)
    
resultado = suma(3, 5)
print(resultado) #None

def suma(a, b):
    # Se utiliza la palabra reservada return para devolver el valor al exterior
    return a+b

resultado = suma(3, 5)
print(resultado) #8

def funcionContar(a):
    for i in range(a):
        if i == 3:
            return 3
        print(i)
        
ultimo_valor = funcionContar(5)
print(f'El ultimo valor es {ultimo_valor}') #3
ultimo_valor = funcionContar(10)
print(f'El ultimo valor es {ultimo_valor}') #3
ultimo_valor = funcionContar(2)
print(f'El ultimo valor es {ultimo_valor}') #None