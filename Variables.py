
#📌Esta línea pide al usuario que escriba su nombre.
#🧠 input() detiene el programa hasta que el usuario responda.
#📝 Lo que escriba se guarda en la variable nombre_alumno y en nivel

nombre_alumno= input("Ingrese su nombre: ")


#📌 Aquí le pedimos al usuario que indique su nivel de conocimiento sobre Python.
#📝 El valor ingresado se guarda en la variable nivel.


nivel= input("Ingrese su nivel de conocimiento (básico, intermedio, avanzado): ")




#📌 Imprime el nombre que ingresó el usuario.
#🔸 El \n al inicio genera un salto de línea para que el texto quede más ordenado
print("\nNombre del alumno:", nombre_alumno)

#📌 Este print usa una f-string, una forma moderna de insertar variables en texto
print(f"Nivel de conocimiento:{nivel} \n")


#📌 Da un mensaje adaptado al nivel del usuario. Aunque siempre dice que empezará desde lo básico, puedes personalizarlo
print(f"Hola {nombre_alumno }, bienvenido al curso de Python.")
print(f"Tu conocimiento es {nivel}, comenzaremos con un repaso de los conceptos básicos.")



#ejemplo 

nombre_astronauta = ("Juan")

edad_astronauta =  32

destino = ("Marte")

print(f"Hola, soy {nombre_astronauta},tengo{edad_astronauta} años y mi proximo destino es {destino}")


combustible = 100

velocidad = 50

print(f"Estoy navegando a{velocidad} km/s con {combustible} % de combustible restante hacia {destino}")
print("Diario de un Astronauta\n")
 
print("Fecha: 2024-01-10")
print("Hoy experimentamos con el cultivo de plantas en microgravedad.")
print("Mensaje personal: ¡Es increíble ver cómo crecen las lechugas aquí arriba!\n")
 
print("Fecha: 2024-01-11")
print("Realizamos una caminata espacial para reparar un panel solar.")
print("Mensaje personal: Flotar en el espacio nunca deja de asombrarme.\n")
