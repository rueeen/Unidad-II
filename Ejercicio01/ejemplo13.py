#ejemplo while

#while es una instruccion para realizar CICLOS

contador = 0

while contador < 10:
    #cuerpo del while y se repite en cada ciclo
    print(f'ejecutando {contador} veces')
    contador += 1
    #dentro del cuerpo siempre debe existir algo que termine la condicion
    
#contador al final vale 10
while contador != 10:
    print('nunca se ejecuta')

print('Si se ejecuta')
#Esto se ejecuta hasta el infinitp
#while True:
#    print('Esto se ejecuta hasta el infinito')

#Esto da error
#while contador < 100:
#    print('algo')
#print('fuera')
#    print('dentro')

#Utilidad de los while true
while True:
    print('----- Menu de acciones ------')
    print('1. Agregar')
    print('2. Modificar')
    print('0. salir')
    
    opcion = input('Ingrese su opcion:\n')
    
    if opcion == '0':
        break
print('Saliendo de programa')