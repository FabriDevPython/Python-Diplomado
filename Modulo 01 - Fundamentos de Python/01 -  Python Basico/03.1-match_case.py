"""
En Python, no existe una estructura case como en otros lenguajes
(como switch en C/Java), pero a partir de Python 3.10
se introdujo la sentencia match-case (similar a un switch).
"""

#1 . Match-case basico
dia = input("Ingrese un dia: ")

match dia:
    case "lunes":
        print("¡Comienza la semana!")
    case "viernes":
        print("¡Ultimo dia laboral!")
    case _: # Default (similar al else)
        print("Dia no reconocido")

# 2. Comparación con valores numéricos
puntaje = int(input("Ingrese puntaje: "))

match puntaje:
    case 100:
        print("Perfecto")
    case 90 | 80 | 70:  # Múltiples valores
        print("Buen trabajo")
    case _ if puntaje < 60:  # Condición adicional
        print("Reprobado")
    case _:
        print("Puntaje válido pero no destacado")