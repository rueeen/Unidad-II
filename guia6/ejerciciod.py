'''
d.	Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

#Datos de entrada
# 10

numero = int(input("Ingrese un numero\n"))

while numero <= 0:
    numero = int(input("Numero incorrecto, intente nuevamente\n"))
    
for i in range(1, numero+1):
    final = ", "
    if i == numero or i == numero - 1:
        final = '\n'    
    if i % 2 != 0:
        print(i, end=final)

#Datos de salida
# 1, 3, 5, 7, 9