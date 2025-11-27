"""
Las funciones son bloques de código que pueden ser llamados
cada vez que los necesitemos, sin condición alguna.
Esto nos permite reutilizar y organizar el código de manera
muy eficiente y práctica.

Reusabilidad: tenemos un fragmento de código usado en muchos sitios, la mejor
solución sería pasarlo a una función. Esto nos evitaría tener código
repetido, y que modificarlo fuera más fácil, ya que bastaría con
cambiar la función una vez.

Modularidad: en vez de escribir largos trozos de código,
es mejor crear módulos o funciones que agrupen ciertos
fragmentos de código en funcionalidades específicas,
haciendo que el código resultante sea más fácil de leer.

def nombre_funcion(argumentos):
    codigo
    return retorno
"""

# Funcion sin retorno
def di_hola():
    print("Hola")

di_hola()

# Funcion argumentos de entrada
def di_hola(nombre):
    print("Hola", nombre)

di_hola("Fabrizio")

# Funcion con retorno
def sumar(a, b):
    resultado = a + b
    return resultado # Devuelve el valor

# Usamos funcion
total = sumar(5, 3)
print(total) # Muestra 8

def resta(a, b):
    return a - b

resta(5, 3) # 2


def suma_y_media(a, b, c):
    suma = a + b + c
    media = suma / 3
    return suma, media

suma, media = suma_y_media(9, 6, 3)
print(suma) # 18
print(media) # 6