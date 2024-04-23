# Listas en memoria

lst_a = [2, 4, 6, 8]

lst_b = lst_a #Esto no crea una nueva lista, sino que, son LA MISMA

lst_b.append(10) #[2, 4, 6, 8, 10]

print(lst_a) #[2, 4, 6, 8, 10] aca lo comprobamos

lst_c = lst_a[0:3] #Esto no copia TODA la lista

print(lst_c) #El final es -1

lst_d = lst_a[0:999999999999999] 

print(lst_d) #Copie toda la list pero no es lo mas correcto

#Si quisiera copiar TODA la lista
lst_e = lst_a[:] #Si se omite el final e inicio se toma TODA la lista

#slicing con incremento
lst_f = lst_b[::2]
print(lst_f)

lst_f.insert(2, 999)

print(lst_f)
print(lst_a)

nueva = ''
for i in "palabra":
    nueva = i + nueva
    
print(nueva)

print('Palabra'[::-1])