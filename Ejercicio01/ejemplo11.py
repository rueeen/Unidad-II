'''
Generador de correo electrónico con formato nombre.apellido@correo.cl, 
solicitando los datos al usuario: 
'''
nombre = input('Ingrese su nombre\n')
#formatos para texto
#todo mayuscula
print(nombre.upper())
#todo minuscula
print(nombre.lower())
#Primera mayus resto minus
print(nombre.capitalize())
apellido = input("Ingrese su apellido\n")
correo = nombre.lower() + '.' + apellido.lower() + '@correo.cl'
print(correo)
