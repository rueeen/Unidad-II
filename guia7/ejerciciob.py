'''
b.	Cree una función en python que reciba una palabra, cuente cuantas vocales 
(a, e, i, o, u) hay dentro de la palabra.
'''

def contarVocales(palabra):
    contar = 0
    for c in palabra:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            contar += 1
    
    print(f'Hay {contar} vocales a, e, i, o, u dentro de la palabra {palabra}')
    
p = input('Ingrese una palabra\n').lower()

contarVocales(p)

