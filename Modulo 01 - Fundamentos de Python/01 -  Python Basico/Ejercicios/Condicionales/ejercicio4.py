"""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor
de ellos.
"""
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} es el mayor")
    else:
        print(f"{n3} es el mayor")
else:
    if n2 > n3:
        print(f"{n2} es el mayor")
    else:
        print(f"{n3} es el mayor")
