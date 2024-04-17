#Scope en python

nombre = "Perico"

def cambiarNombre():
    nombre = "Maria"
    print(nombre)
    
cambiarNombre()    
    
print(nombre)#Perico

#Variable global
def cambiarNombreGlobal():
    global nombre
    nombre = "Maria"
    
cambiarNombreGlobal()
    
print(nombre)