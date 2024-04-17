n = int(input('Ingrese un numero cualquiera\n'))
m = int(input('Ingrese otro numero\n'))

if n > m:
    print(f'el mayor es: {n}')
elif m > n:
    print(f'el mayor es: {m}')
else:
    print('Son iguales')