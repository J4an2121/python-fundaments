#En Python, scope significa el alcance o la visibilidad de una variable, es decir, desde dónde puedes usar esa variable en tu programa.

#Piensa en scope como las "fronteras" que tiene cada variable.








#Local → dentro de funciones.
def func():
    var_local = "Soy una variable local"
    print(var_local)

func()  # Llama a la función para mostrar la variable local



#Enclosing → funciones dentro de funciones.

def func_externa():
    var_enclosing = "Soy una variable de la función externa"

    def func_interna():
        print(var_enclosing)

    func_interna()

func_externa()

#Global → disponibles en todo el archivo.


variable_global = "Soy una variable global"

for i  in range(10):
    print(variable_global)  # Imprime la variable global en cada iteración



#Built-in → funciones/variables propias de Python.
