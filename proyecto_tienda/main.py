#importaciones
import os

#funciones
def buscarProducto(nombre, lista):
    for p in lista:
        if p['nombre'] == nombre:
            return p #retorna un diccionario con keys nombre y precio
    return None #si no encontramos el nombre retornamos None

# declarar 2 listas
tienda = []
venta = []

# menu de acciones
while True:
    os.system('cls')
    print('==== Menu opciones ====')
    print('1. Agregar productos')
    print('2. Modificar precio producto')
    print('3. Listar productos tienda')
    print('4. Eliminar producto')
    print('5. Agregar venta')
    print('6. Mostrar total')
    print('0. Salir')
    
    op = input('Ingrese opcion a realizar:\n')
    os.system('cls')
    if op == '1':
        print('==== Agregar producto ====')
        nombre = input('Ingrese nombre producto\n') #Se valida que nombre sea unico
        
        r = buscarProducto(nombre, tienda)
        
        if r is None:
            try:
                precio = int(input('Ingrese precio producto\n'))
                producto = {'nombre':nombre, 'precio':precio}
                tienda.append(producto)
                print('Se agrego producto')
            except:
                print('Ingrese un valor no valido')
        else:
            print('Producto ya existe')
            
    elif op == '2':
        print('==== Modificar precio ====')
        nombre = input('Ingrese nombre a modificar\n')
        nuevo_precio = int(input('Ingrese precio a modificar\n'))
        
        r = buscarProducto(nombre, tienda)
        
        if r is not None:
            #r es un diccionario devuelto por la funcion
            r['precio'] = nuevo_precio
            print('Se ha modificado el precio del producto')
        else:
            print('Producto no existe')
            
    elif op == '3':
        print('==== Lista tienda ====')
        if len(tienda) == 0:
            print('No hay productos')
        else:
            for p in tienda:
                print(f'Nombre: {p["nombre"]}')
                print(f'Precio: {p["precio"]}')
                print('------------------------------------------------')
                
    elif op == '4':
        print('==== Eliminando producto ====')
        nombre = input('Ingrese nombre a eliminar\n')
        
        r = buscarProducto(nombre, tienda)
        
        if r is not None:
            resp = input(f'Esta seguro que desea elimianr {r["nombre"]}?').lower()
            if resp == 'si':
                tienda.remove(r)
                print(f'Se elimino producto {r["nombre"]}')
            else:
                        print('No se elimino')
        else:
            print('No se encontro el producto en la tienda')
        
        

    elif op == '5':
        print('==== Agregar venta ====')
        nombre = input('Ingrese producto a comprar\n')
        r = buscarProducto(nombre, tienda)
        if r is not None:
            venta.append(r)
            print('Se agrego producto a carrito venta')
        else:
            print('Producto no encontrado')
            
    elif op == '6':
        print('==== Total ventas ====')
        if len(venta) == 0:
            print('No hay ventas aun')
        else:
            total = 0
            for p in venta:
                print(f'{p["nombre"]}............ {p["precio"]}')
                total += p['precio']
            
            print('_______________________________________________')
            print(f'Total venta: {total}')
        
        
    input('Presione ener para continuar...') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
flag = False
for p in tienda:
    if p['nombre'] == nombre:
        flag = True
        
        
if flag == False:
    #Agregamos producto
else:
    #Se envia mensaje indicando duplicidad
'''
        
        
        
        
        
        
        
        
        
        
        