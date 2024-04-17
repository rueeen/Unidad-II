# Funciones con parametros definidos

def sumar(a=5, b=8):
    print(a+b)
    
sumar(3) #11
sumar(b=3) #8
sumar() #13
sumar(2, 2) #4