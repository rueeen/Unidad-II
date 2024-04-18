'''
1.	Cree un script en Python con una función que tenga retorno y que, al recibir una palabra o frase, 
la devuelva con el siguiente reemplazo de caracteres: (12 puntos)
b, B = 8 
S, s = $ 
G, g = 6
L, l = 7
U, u = x
'''
#Funciones siempre al inicio
def cambiarLetras(p):
    nueva_palabra = ''
    for c in p:
        if c == 'S' or c == 's':
            nueva_palabra += '$'
            
        elif c == 'b' or c == 'B':
            nueva_palabra += '8'
            
        elif c == 'g' or c == 'G':
            nueva_palabra += '6'
            
        elif c == 'l' or c == 'L':
            nueva_palabra += '7'
            
        elif c == 'u' or c == 'U':
            nueva_palabra += 'x'
            
        else:
            nueva_palabra += c
            
    return nueva_palabra

#Dato entrada
palabra = input('Ingrese una palabra\n')

#Invocacion funcion
solucion = cambiarLetras(palabra)
print(solucion)

#Por 5 decimas
#Invertir una palbara con ciclo for
#entrada -> hola
#salida  -> aloh