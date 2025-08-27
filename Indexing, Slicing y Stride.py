# 📋 Lista de tareas (mutable, ordenada, permite cambios)
lista_tareas = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

# 📦 Tupla de tareas (inmutable, ordenada, no se puede modificar)
tupla_tareas = ("tarea1", "tarea2", "tarea3", "tarea4", "tarea5")

# 📚 Diccionario de tareas (clave: valor)
dic_tareas = {
    "tarea1": "pendiente",
    "tarea2": "en proceso",
    "tarea3": "pendiente",
    "tarea4": "terminada",
    "tarea5": "en proceso"
}

#selecionar un dato de la lista

print("Lista de tareas:", lista_tareas[0])  # Acceso al primer elemento de la lista

print("Tupla de tareas:", tupla_tareas[1])  # Acceso al segundo elemento de la tupla

print("Estado de tarea1:", dic_tareas["tarea1"])  # Acceso al valor de la clave "tarea1" en el diccionario