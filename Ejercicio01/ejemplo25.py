#Mas metodos de listas

#clear

lst = [1, 23, 4, 5, 54, 545, 454, 5, 4, 5, 45, 4, 5, 54]

print(lst)
#Esto borra completamente la lista de memoria pero NO SU CONTENIDO
#del lst

lst.clear() #Este metodo VACIA la lista []

print(lst)

#Otra forma de agregar
lst.append(2) #Agrega 2 a la lista
print(lst)
lst.append(3) #[2, 3]
print(lst)
#insert agrega en una posicion fija un valor a la lista
lst.insert(1, 4) # [2, 4, 3]
print(lst)

#Metodo index
indice = lst.index(4) #1
print(indice)

#indice = lst.index(5) da error porque 5 no esta como valor en la lista
lst = [2, 4, 3, 5, 4]
indice = lst.index(4) #
print(indice)

#remove
#Elimina por VALOR
lst.remove(3)
print(lst) #[2, 4, 5, 4]

#lst.remove(6) error
lst.remove(4) #Elimina el primer 4 que encuentra
print(lst) #[2, 5, 4]