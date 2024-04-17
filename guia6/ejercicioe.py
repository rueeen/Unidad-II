'''
a.	Crear un script en Python que solicite una palabra, 
cuente cuantos caracteres “a” hay en la palabra. 
'''
#dato entrada
palabra = input('Ingrese una palabra\n').lower()
#hola
contar = 0

for c in palabra:
    # c = h
    # c = o
    # c = l
    # c = a
    if c == "a":
        contar += 1

#dato salida
# hay '1' caracter(es) "a" en la palabra "hola"
print(f'Hay \'{contar}\' caracter(es) "a" en la palabra "{palabra}"')