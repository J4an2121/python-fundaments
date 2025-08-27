#for <variable> in <iterable>:
  # <sentencias>

lista = ["tarea1", "tarea2", "tarea3"]
 
for tarea in lista:
    print("Estoy trabajando en la tarea", tarea)



#Bucle for

#Sirve para repetir un bloque de código un número determinado de veces o recorrer elementos de una colección (lista, tupla, cadena, etc.).

#Sintaxis:

#for variable in secuencia:
    # Código que se repite


#Ejemplo:

frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)


#Bucle while

#repite un bloque de código mientras una condición sea verdadera.

#Sintaxis:

#while condición:
    # Código que se repite
#Ejemplo:

# Contador que inicia en 1 y se incrementa hasta 5

contador = 1
while contador <= 5:
    print(contador)
    contador += 1


#break

#Sirve para detener un bucle antes de que termine normalmente.

#Ejemplo:

for numero in range(1, 10):
    if numero == 5:
        break
    print(numero)

#continue

#Sirve para saltar la iteración actual y seguir con la siguiente.

#Ejemplo:

for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)