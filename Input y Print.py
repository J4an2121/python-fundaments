
#print() es una función que muestra texto en la pantalla.

print("hola, bienvenido a mi programa")

 #Puedes imprimir varios textos juntos separándolos con comas.
print("hola, bienvenido a mi programa." ,"clase 1")

#sep="-" indica que queremos usar un guion como separador entre los textos.

print("hola, bienvenido a mi programa.", "clase 2", sep="-")#


#end="\n\n" agrega dos saltos de línea al final.
print("hola, bienvenido a mi programa.", "clase 1", sep="-", end="\n\n") # salto de linea
print("fundamentos de python:")

#input() permite al usuario escribir su nombre.
#Luego lo combinamos en un mensaje usando print().
print("hola",input("Introduce tu nombre:") ,"bienvenido al curso de python")