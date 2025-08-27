#En Python, cuando algo sale mal (por ejemplo dividir entre cero, leer un archivo que no existe, etc.), el programa se detiene y aparece un error.
#👉 Para evitar que el programa se rompa, usamos el manejo de excepciones con try y except.


try:
    print(var)
except :
    print("la variable no está definida")

print("Programa sigue ejecutandose")
