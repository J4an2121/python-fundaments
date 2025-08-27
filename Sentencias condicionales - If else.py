edad = int(input("¿Cuál es tu edad? "))
if edad >= 18 and edad < 21:
    print("Eres mayor de edad en Colombia")
elif edad >= 21:
    print("Eres mayor de edad en USA")
else:
    print("Eres menor de edad.")


    edad = int(input("¿Cuál es tu edad? "))

# ejemplo 

edad = int(input("¿Cuál es tu edad? "))

if edad < 5:
    print("Entrada gratis 👶")
elif edad < 18:
    print("Entrada con descuento 🎟️")
elif edad < 60:
    print("Entrada normal 💰")
else:
    print("Entrada para adulto mayor 👴")

#ejmplo 

nota = float(input("Ingresa tu nota: "))

if nota >= 90:
    print("Excelente 😎")
elif nota >= 75:
    print("Bueno 👍")
elif nota >= 60:
    print("Aprobado 😅")
else:
    print("Reprobado ❌")



    # in 
    #Sirve para comprobar si un elemento existe dentro de una secuencia 
    #(puede ser lista, tupla, cadena, conjunto, etc.)


    #ejemplo


    # Definir la tupla con los niveles de amenaza
niveles_amenaza = ("bajo", "moderado", "alto", "crítico")

# Asignar un nivel de amenaza actual
amenaza_actual = "bajo"

# Verificar si el nivel ingresado está en la tupla
if amenaza_actual in niveles_amenaza:
    # Imprimir el nivel actual
    print(f"Nivel de amenaza actual: {amenaza_actual}")  
    
    #La f antes de las comillas indica que es una f-string (cadena formateada).
   #Esto permite insertar variables directamente dentro del texto usando {}.
   # Si amenaza_actual = "bajo", el resultado será:


    # Recomendación según el nivel
    if amenaza_actual == "bajo":
        print("Actividad recomendada: Realizar auditorías de seguridad regulares.")
    elif amenaza_actual == "moderado":
        print("Actividad recomendada: Reforzar la concienciación de los empleados sobre riesgos de Ciberseguridad.")
    elif amenaza_actual == "alto":
        print("Actividad recomendada: Implementar medidas de seguridad adicionales y revisar accesos.")
    elif amenaza_actual == "crítico":
        print("Actividad recomendada: Activar el protocolo de respuesta a incidentes.")
else:
    print("Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico).")