#datos de entrada
peso = float(input('Ingrese su peso\n'))
altura = float(input('Ingrese su altura\n'))

#proceso calculo imc
imc = peso / altura ** 2

#proceso de comparacion 
if imc <= 15:
    #dato salida
    print('Delgadez muy severa.')
elif imc > 15 and imc <= 15.9:
    #dato salida
    print('Delgadez severa')
elif imc < 18.4:
    #dato salida
    print('Delgadez')
elif imc < 24.9:
    #dato salida
    print('Peso saludable')
elif imc < 29.9:
    #dato salida
    print('Sobrepeso')
elif imc < 34.9:
    #dato salida
    print('Obesidad moderada')
elif imc < 39.9:
    #dato salida
    print('Obesidad severa')
else:
    #dato salida
    print('Obesidad muy severa')