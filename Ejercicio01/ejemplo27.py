#Creando un diccionario

diccionario = {} #0 elementos

dict_nombres = {'Nombre1':'Perico', 'Nombre2':'Maria'} #2 elementos

print(dict_nombres)

#Las llaves o keys son UNICAS
dict_nombres = {'Nombre1':'Perico', 'Nombre2':'Maria', 'Nombre1': 'Periquin'} 

print(dict_nombres)

#Para acceder al valor de una llave
print(dict_nombres['Nombre2'])

#QUe podemos utilizar como llaves ?
dict_mixto = { 0: 'valor 1', 'nombre':'Perico', True: 'aca esta el valor true' , False:'Reemplazamos al valor 1', 1:'Este reemplaza al TRue'}
print(dict_mixto)