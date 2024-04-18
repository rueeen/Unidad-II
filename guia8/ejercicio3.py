# dato entrada -> palabra1 y p l b                2
# dato salida  -> palabra1 tiene mas caracteres que plb2

def mostrarPalabraMayor(p1, p2):
    c_p1 = 0
    c_p2 = 0
    
    for c in p1:
        if c != ' ':
            c_p1 += 1
            
    for c in p2:
        if c != ' ':
            c_p2 += 1
            
    if c_p1 > c_p2:
        print(f'{p1} es mas larga que {p2}')
    elif c_p1 < c_p2:        
        print(f'{p2} es mas larga que {p1}')
    else:
        print("Son del mismo tamaño")

palabra1 = input('Ingrese una palabra\n')
palabra2 = input('Ingrese otra palabra palabra\n')

mostrarPalabraMayor(palabra1, palabra2)
