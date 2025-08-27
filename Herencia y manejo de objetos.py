#1. ¿Qué es la Herencia?

#La herencia permite que una clase (hija) reutilice atributos y métodos de otra clase (padre).

#Es como en la vida real:

#Un Animal puede ser padre.

#Un Perro o un Gato son hijos, heredan lo básico de Animal, pero también tienen cosas propias.

#👉 Ventaja: No repetir código y organizar 

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Clase Hija (hereda de Animal)
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

# Clase Hija (hereda de Animal)
class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Crear objetos
mi_perro = Perro("Firulais")
mi_gato = Gato("Misu")

mi_perro.comer()   # Heredado de Animal
mi_perro.ladrar()  # Propio de Perro
mi_gato.comer()    # Heredado de Animal
mi_gato.maullar()  # Propio de Gato


#Manejo de Objetos

#Un objeto es como una copia real de la clase.
#Con ellos puedes:

#Crear instancias (copias de la clase).

#Acceder a atributos.

#Usar métodos.

#Modificar valores.

#👉 Ejemplo práctico:

# Clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear objetos
persona1 = Persona("Juan", 32)
persona2 = Persona("Paula", 28)

# Usar métodos
persona1.presentarse()
persona2.presentarse()

# Cambiar atributo
persona1.edad = 33
print(f"{persona1.nombre} ahora tiene {persona1.edad} años.")