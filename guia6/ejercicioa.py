'''
e.	Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
'''

numero = int(input('Ingrese un numero\n'))

while numero <= 0:
    numero = int(input('Error. Intente nuevamente\n'))
    
for i in range(numero, -1, -1):
    final = ", "
    if i == 0:
        final = "\n"
    print(i, end=final)