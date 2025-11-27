"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
contador = 1
mayores_iguales_7 = 0
menores_7 = 0

while contador <= 10:
    nota = int(input("Ingrese una nota: "))
    contador += 1

    if nota >= 7:
        mayores_iguales_7 += 1
    else:
        menores_7 += 1

print(f"Cantidad de notas mayores o iguales a 7: {mayores_iguales_7}")
print(f"Cantidad de notas menores a 7: {menores_7}")