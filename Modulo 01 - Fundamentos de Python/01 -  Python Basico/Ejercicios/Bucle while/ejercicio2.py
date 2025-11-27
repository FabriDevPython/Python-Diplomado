"""
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
altura promedio de las personas.
"""
# Pedimos al usuario la cantidad de alturas que se van a ingresar
n = int(input("¿Cuantas alturas quiere ingresar? "))

# Inicializamos un contador para saber cuántas veces se ha repetido el bucle
contador = 1

# Inicializamos un acumulador en 0 para ir sumando todas las alturas
suma_alturas = 0 

# El bucle se ejecutará mientras el contador sea menor o igual a 'n'
while contador <= n:

    # Solicitamos al usuario que ingrese una altura en cada iteración
    altura = int(input("Ingrese la altura en centimetros: "))

    # Sumamos la altura ingresada a nuestro acumulador
    suma_alturas += altura
    
    # Incrementamos el contador en 1 para avanzar en el bucle
    contador += 1

# Una vez que el bucle termina, calculamos el promedio
promedio = suma_alturas / n

# Mostramos el resultado final
print(f"La altura promedio de las personas es: {promedio}")