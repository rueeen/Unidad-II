'''
c.	Cree una función en python que reciba un número, escriba si el número es par o impar.
'''

def parImpar(n): 
    if n % 2 == 0:
        print("es par")
    else:
        print("es impar")
        
numero = int(input('Ingrese un numero entero positivo\n'))

while numero <= 0:
    numero = int(input('Debe ingresar un numero positivo\n'))
    
parImpar(numero)