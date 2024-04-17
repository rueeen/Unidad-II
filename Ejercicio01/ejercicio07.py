#Calcular la suma de 4 números con decimales ingresados por el usuario: 
n1 = float(input("Ingrese un numero\n"))
n2 = float(input("Ingrese un numero\n"))
n3 = float(input("Ingrese un numero\n"))
n4 = float(input("Ingrese un numero\n"))

resultado = n1 + n2 + n3 + n4
#Imprimir resultado con propiedad sep de print
print("El resultado de la suma es", resultado)
#Imprimir concatenando
print("El resultado de la suma es "+str(resultado))
#Format de print
print(f"El resultado de la suma es {resultado}")