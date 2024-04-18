# Entrada -> 5
# Salida  -> 55555
#            4444
#            333
#            22
#            1
print('con for')
numero = int(input("Ingrese un numero\n"))
#Con for
for i in range(numero, 0, -1):
    print(str(i)*i)
    
print('con while')
while numero > 0:
    auxiliar = numero
    while auxiliar > 0:
        print(numero, end='')
        auxiliar -= 1
    print()
    numero -= 1
