"""
Un bucle for en programación es una estructura de control que se utiliza
para iterar sobre una secuencia de elementos iterables, como listas, tuplas,
rangos de números, etc. Su función es ejecutar un bloque de código repetidamente
con cada elemento de la secuencia.
"""
for x in range(101):
    print(x)

for x in range(20,31):
    print(x)

for x in range(1,100,2):
    print(x)

for i in "Python":
    print(i)

"""
Los iterables: Objetos que pueden ser iterados (indexados). Si pensas
en una lista, podemos indexarlo con lista[1], seria un iterable.

Los iteradores: Objetos que hacen referencia a un elemento, y que tienen
un metodo next que permite hacer referencia al siguiente.

Los objetos que pueden ser iterable son: listas, tuplas, conjuntos, diccionarios
cadenas(string).
"""
# Iterables
numero = "10"

for i in numero:
    print(i)


# Iteradores
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


print(list(range(5, 20, 2)))

for i in range(5, 20, 2):
    print(i)

for i in range(5, 0 , -1):
    print(i)

suma = 0
for f in range(10):
    valor = int(input("Ingrese valor:"))
    suma = suma + valor
print(f"La suma es {suma}")

promedio = suma / 10
print(f"El promedio es: {promedio}")


aprobados=0
reprobados=0
for f in range(10):
    nota=int(input("Ingrese la nota:"))
    if nota>=7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1
print("Cantidad de aprobados")
print(aprobados)
print("Cantidad de reprobados")
print(reprobados)


mul3 = 0
mul5 = 0
for f in range(10):
    valor = int(input("Ingrese un valor:"))
    if valor % 3 == 0:
        mul3 = mul3 + 1
    if valor % 5 == 0:
        mul5 = mul5 + 1
print(f"Cantidad de valores ingresados múltiplos de 3 {mul3}")

print(f"Cantidad de valores ingresados múltiplos de 5 {mul5}")


cantidad = 0
n = int(input("Cuantos valores ingresará:"))
for f in range(n):
    valor = int(input("Ingrese el valor:"))
    if valor >= 1000:
        cantidad = cantidad + 1
print("La cantidad de valores ingresados mayores o iguales a 1000 son")
print(cantidad)

