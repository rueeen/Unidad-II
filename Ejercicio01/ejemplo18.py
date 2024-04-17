#Argumento posicional
def dividir_2_numeros(a, b):
    print(f'El resultado es {a/b}')
    
dividir_2_numeros(3, 6) #0.5
dividir_2_numeros(6, 3) #2.0

#Keyword arguments
dividir_2_numeros(b=3, a=6) #2.0
#dividir_2_numeros(b=3, c=6) #error c no existe como parametro
#dividir_2_numeros(b=3, 6) # si tengo argumento por keyword, por OBLIGACION el siguiente argumento tambien es de KEYWORD
#dividir_2_numeros(3, a=6) # error multiples argumentos para a