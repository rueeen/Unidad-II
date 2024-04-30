#mis 2 listas para trabajr
ticket_abiertos= [] #lista vacia
ticket_cerrados = [] #lista vacia

def buscarTicket(codigo, lista):
    for t in lista:
        if t['codigo'] == codigo:
            return t
    return

while True:
    print('==== Menu de opciones ====')
    print('1. Crear ticket')
    print('2. Mostrar tickets abiertos')
    print('3. Cerrar ticket')
    print('4. Mostrar tickets cerrados')
    print('5. Eliminar tickets cerrados')
    print('0. Salir')
    
    op = input('Ingrese su opcion\n')
    
    if op == '1':
        print('==== Crear ticket ====')
        codigo = input('Ingrese codigo ticket\n').upper()
        if len(codigo) > 4:
            print('Error: Codigo debe tener 4 caracteres como maximo')
        else:
            titulo = input('Ingrese titulo ticket\n').capitalize()
            ticket = {'codigo':codigo, 'titulo':titulo}
            ticket_abiertos.append(ticket) #agregamos diccionario ticket a la lista
            print('Ticket agregado con exito')
    
    elif op == '2':
        print('==== Lista tickets abiertos ====')
        #print(ticket_abiertos) caca no se hace
        if len(ticket_abiertos) == 0:
            print('No hay tickets abiertos')
        else:
            for t in ticket_abiertos:
                print(f'Codigo: {t["codigo"]}')
                print(f'Titulo: {t["titulo"]}')
                print('-----------------------------------')
                
    elif op == '4':
        print('==== Lista tickets cerrados ====')
        #print(ticket_abiertos) caca no se hace
        if len(ticket_cerrados) == 0:
            print('No hay tickets cerrados')
        else:
            for t in ticket_cerrados:
                print(f'Codigo: {t["codigo"]}')
                print(f'Titulo: {t["titulo"]}')
                print(f'Comentario: {t["comentario"]}')
                print('-----------------------------------')
        
    elif op == '3':
        print('==== Cerrando ticket ====')
        codigo = input('Ingrese codigo a cerrar\n').upper() # hola -> HOLA
        
        respuesta = buscarTicket(codigo, ticket_abiertos) #Devuelve None o un diccionario ticket
        
        if respuesta is not None:
            respuesta['comentario'] = input('Ingrese un comentario al ticket\n')
            ticket_cerrados.append(respuesta)
            ticket_abiertos.remove(respuesta)
            print('Se ha cerrado ticket')
        else:
            print('No se encontro ticket en la lista')
    
    elif op == '5':
        print('==== Limpiando cerrados ====')
        respuesta = input('Esta seguro que desea vaciar la lista?\n').lower()
        
        if respuesta == 'si':
            ticket_cerrados.clear()
            print('Se limpio lista de tickets')
        else:
            print('No se hizo nada')
            
    elif op == '0':
        print('Saliendo del programa')
        break
    
    else:
        print('Opcion ingresada no valida')        
        
        