#Recorriendo listas
lst = [324, 32, 443, 55]
#       0    1   2    3

#Recorriendo por valor
for v in lst:
    print(v)
    
#Recorrer por indice
#        range(4) -> 0, 1, 2, 3
for i in range(len(lst)):
    print(f'Su indice es {i} y su valor es {lst[i]}')