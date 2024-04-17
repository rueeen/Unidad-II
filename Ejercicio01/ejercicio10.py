#Conversor de longitud (Pies a Metros) solicitando los datos al usuario: 

pies = float(input("Ingrese pies a convertir\n"))

metros = pies * 0.3040
#round para redondear
print(f'Los {pies} pies a metros son {round(metros, 2)}')