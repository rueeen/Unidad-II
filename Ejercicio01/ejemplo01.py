#Variables en python
#nombre variable luego un = y finalmente el valor

nombre = "Perico" #De tipo String (cadena)
apellido = 'Los palotes' #De tipo String (cadena)
edad = 35 #de tipo int (entero)

#el keyword sep permite cambiar como se separan los parametros, por defecto
#es un espacio vacio " "
print(nombre," ", apellido, " ", edad, sep='---')
print('aca no hay salto de linea', end='')
print(nombre, apellido, edad)
#el salto de linea se codifica como \n
print('aca hay un salto de linea', end='\n')

#print(parametros, sep=" ", end="\n")

