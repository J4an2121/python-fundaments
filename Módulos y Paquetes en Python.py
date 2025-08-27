#Un módulo es simplemente un archivo .py que contiene funciones, 
# clases o variables que puedes reutilizar en otros programas.

# archivo: matematicas.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
#En otro archivo:

#python
#Copiar
#Editar
#import matematicas

#print(matematicas.sumar(5, 3))   # 8
#print(matematicas.restar(5, 3))  # 2


#🔹 Paquetes

#Un paquete es una carpeta que contiene varios módulos.
#Debe incluir un archivo especial llamado __init__.py (aunque en versiones modernas puede estar vacío).