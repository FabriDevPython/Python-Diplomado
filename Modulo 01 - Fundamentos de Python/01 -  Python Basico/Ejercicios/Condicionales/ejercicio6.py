"""
Confeccionar un programa que permita cargar un número entero positivo de
hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
Mostrar un mensaje de error si el número de cifras es mayor
"""

numero = int(input("Ingrese un numero positivo de 1 / 2 / 3 cifras: "))

if numero < 10:
    print("Tiene una cifra")
else:    
    if numero < 100:
        print("Tiene dos cifras")
    else:
        if numero < 1000:
            print("Tiene tres cifras")