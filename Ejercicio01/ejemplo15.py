#Operadores utiles

# break
# break permite romper ciclos cuando se ejecuta

contador = 0
while contador < 100000000000000000:
    print(contador)
    contador+=1
    
    if contador == 5:
        #Ejecutando bloque break
        break
        print("ESTO NUNCA SE EJECUTA")

print('Esto se ejecuta luego del break')

# Continue
# Este operador detiene el ciclo actual y pasa al siguiente
for i in range(10):
    if i == 4:
        continue
    print(i)