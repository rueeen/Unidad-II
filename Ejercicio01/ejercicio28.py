#Agregando pares ordenados a un diccionarios

dict_nombres = {'Nombre1':'Perico'}

#Forma 1
dict_nombres['Nombre1'] = 'Maria' #Reemplazamos a Perico por Maria

dict_nombres['Nombre2'] = 'Perico' #AGREGA una nueva KEY con su VALUE

print(dict_nombres)

nuevo_nombre = input('Ingrese un nuevo nombre\n')
nueva_key = input('Nueva key\n')

dict_nombres[nueva_key] = nuevo_nombre

print(dict_nombres)

#Forma 2
dict_nombres.update({'Nombre4':'Nuevo valor', 'Nombre5':'Se agregaron 2 elementos'})

print(dict_nombres)

#Metodos adicionales
#Copy crea un nuevo diccionario en memoria
d1 = dict_nombres #SON LO MISMO
nuevo_dict = dict_nombres.copy() #Crear una copia del diccionario

#Eliminar datos de un diccionario con del
del dict_nombres['Nombre2'] 
print(dict_nombres)

eliminado = dict_nombres.pop('Nombre4')
print(dict_nombres)
print(eliminado)

dict_nombres.popitem()