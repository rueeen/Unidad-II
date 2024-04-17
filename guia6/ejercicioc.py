'''
c.	Genere un archivo llamado repetir.py que solicite al usuario una palabra y una cantidad. 
Posteriormente debe mostrar por pantalla la palabra repetida la cantidad de veces escrita.
'''

palabra = input("Ingrese una palabra\n")
cantidad = int(input("Ingrese una cantidad\n"))

#Sin ciclos
print((palabra+"\n")*cantidad)

print()

while cantidad > 0:
    print(palabra)
    cantidad -= 1
    

