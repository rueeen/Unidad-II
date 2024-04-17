'''
Conversor de monedas (Dólar a CLP) solicitando el valor actual 
del dólar y la cantidad de dolares al usuario: 
'''

chilenos = 940.80
dolares = int(input('Ingrese cantidad de dolares a convertir\n'))

total = dolares * chilenos

print(f'Los {dolares} dolares a pesos chilenos es {total}')