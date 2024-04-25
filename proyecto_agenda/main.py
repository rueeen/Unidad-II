'''
Proyecto agenda
Requerimientos:
1. Que la agenda registre personas en una lista
   a. Datos necesarios: nombre, apellido, numero
2. Que las personas agregadas esten en formato diccionario
3. Que se pueda mostrar la agenda completa
4. Que se puedan eliminar personas de la agenda
5. Que se puedan buscar peronas en la agenda
'''
def buscarContacto(nombre, apellido, lista):    
    for c in lista:
        if c['nombre'] == nombre and c['apellido'] == apellido:
            return c
    return None
    
agenda = [] #lista vacia

while True:
    print('==== Menu de opciones ====')
    print('1. Agregar contacto')
    print('2. Mostrar agenda')
    print('3. Eliminar contacto')
    print('4. Modificar contacto')
    print('0. Salir') 
    
    opcion = input('Ingrese su opcion\n')
    #Agregando personas
    if opcion == '1':
        print('==== Agregando Contacto ====')
        nombre = input('Ingrese su nombre\n').capitalize()
        apellido = input('Ingrese su apellido\n').capitalize() 
        numero = int(input('Ingrese su numero de telefono\n')) #Validar que sean 8 numeros ingresados
        
        contacto = {'nombre':nombre, 'apellido':apellido, 'numero':numero}
        
        agenda.append(contacto)
        
        print(f'Se agrego el contacto {nombre} {apellido}')
        
    elif opcion == '2':
        print('==== Lista contactos ====')
        if len(agenda) == 0:
            print('No existen contactos aun')
        else:
            for c in agenda:
                print(f'Nombre: {c["nombre"]}')
                print(f'Apellido: {c["apellido"]}')
                print(f'Numero: {c["numero"]}')
                print('-----------------------------------------------')
            
    elif opcion == '3':
        print('==== Eliminar contacto ====')
        nombre = input('Ingrese nombre de contacto a eliminar\n').capitalize()
        apellido = input('Ingrese apellido de contacto a eliminar\n').capitalize()
        
        respuesta = buscarContacto(nombre, apellido, agenda)
        
        if respuesta is not None:
            print("Contacto encontrado")
            agenda.remove(respuesta)
        else:
            print("No se encontro contacto")
            
    elif opcion == '4':
        print('==== Modificar contacto ====')
        nombre = input('Ingrese nombre a modificar\n').capitalize()
        apellido = input('Ingrese apellido a modificar\n').capitalize
        
        resultado = buscarContacto(nombre, apellido, agenda)
        
        if resultado is not None:
            print('1. Modificar nombre')
            print('2. modificar apellido')
            print('3. modificar numero')
            
            opcion = input('Ingrese su opcion\n')
            
            if opcion == '3':
                numero = int(input('Ingrese nuevo numero\n'))  #Validar que sean 8 numeros ingresados
                
                resultado['numero'] = numero
                
                print('Numero modificado')
                
        else:
            print('Contacto no encontrado')