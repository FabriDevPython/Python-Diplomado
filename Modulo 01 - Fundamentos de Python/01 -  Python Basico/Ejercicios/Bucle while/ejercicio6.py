"""
Desarrollar un programa que permita cargar n números enteros y luego nos
informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este
operador retorna el resto de la división de dos valores, por ejemplo 11%2
retorna un 1):
 if valor%2==0: 
"""

n = int(input("Ingrese cuantos numeros quiere cargar: "))

contador = 1
pares = 0
impares = 0

while contador <= n:
    numero = int(input("Ingrese un numero par/impar: "))
    contador += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Los numeros pares que hay: {pares}")
print(f"Los numeros impares que hay son: {impares}")
