'''
a.	Cree una función en python que reciba 2 números, imprima un mensaje con el mayor de ellos.
'''

def elMayor(a, b):
    if(a > b):
        print(a, "es mayor")
    elif(a == b):
        print('Son iguales')
    else:
        print(b, "es mayor")
        
n = float(input('Ingrese un numero\n'))
m = float(input('Ingrese otro numero\n'))

#Invocando funcion
elMayor(n, m)