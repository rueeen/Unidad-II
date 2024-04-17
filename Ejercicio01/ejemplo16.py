#Funciones

#Las funciones sirven para reutilizar codigo

# instruccion def
# nombre funcion
# parametros 0, 1 o muchos
#saludar() Esto da error
# La funcion debe ser definida antes de ser invocada

def saludar ():
    print('Saludar desde funcion')
    
def saludar_con_nombre (nombre):
    print(f'Su nombre es {nombre}')
    
def sumar_2_numeros (a, b):
    print(f'El resultado es {a+b}')
    
# Una funcion SE INVOCA con su nombre y argumentos a enviar
saludar()
#saludar('perico') esto da error
# Si la funcion se definio SIN PARAMETROS no se envia ARGUMENTO

saludar_con_nombre("perico")
#saludar_con_nombre() Error
# Se necesita 1 argumento para ejecutar este codigo

sumar_2_numeros(5, 2)