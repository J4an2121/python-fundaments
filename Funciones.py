#sintaxis
#def <nombre de la funcion>([parametros]):
#    <sentencias>


#Idea general

#Una función es como una receta de cocina:

#Tiene ingredientes (en Python se llaman parámetros).

#Tiene instrucciones (lo que hace el código).

#Te da un resultado (en Python, eso se logra con return).

def calcular_descuento(precio, descuento):
    valor_descuento = precio * (descuento / 100)
    precio_final = precio - valor_descuento
    return precio_final

precio1 = calcular_descuento(100000, 10)  # producto de 100.000 con 10% de descuento
precio2 = calcular_descuento(75000, 20)   # producto de 75.000 con 20% de descuento

print("El precio final del primer producto es:", precio1)
print("El precio final del segundo producto es:", precio2)