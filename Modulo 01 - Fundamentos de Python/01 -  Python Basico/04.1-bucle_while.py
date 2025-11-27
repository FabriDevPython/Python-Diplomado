"""
Un bucle es una estructura de control de flujo que permite
repetir un bloque de código un número determinado o indeterminado de veces.
Los bucles son elementos necesarios en programación,
ya que permiten ejecutar una tarea concreta varias veces,
sin tener que escribir manualmente el mismo código repetidamente.
"""
# Bucle while
x = 1

while x <= 100:
    print(x)
    x += 1


n = int(input("Ingrese el valor final:"))
x = 1
while x <= n:
    print(x)
    x += 1

# Programa que muestre la tabla del 8 hasta 8 x 10
x = 8

while x <= 80:
    print(x)
    x += 8

x = 1
suma = 0
while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma += valor
    x += 1

promedio = suma / 10

print(f"La suma de los 10 valores es: {suma}")
print(f"El promedio es: {promedio}")


cantidad = 0
x = 1
n = int(input("Cuantas piezas cargara:"))
while x <= n:
    largo = float(input("Ingrese la medida de la pieza:"))
    if largo >= 1.2 and largo <= 1.3:
        cantidad += 1
    x += 1

print(f"La cantidad de piezas aptas son {cantidad}")


x = 5

while x > 0:
    x -= 1
    print(x)
else:
    print("El bucle ha finalizado.")