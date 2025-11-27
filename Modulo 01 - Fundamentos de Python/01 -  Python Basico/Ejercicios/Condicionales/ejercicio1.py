"""
Realizar un programa que solicite la carga por teclado de dos números, si el
primero es mayor al segundo informar su suma y diferencia, en caso contrario
informar el producto y la división del primero respecto al segundo.
"""
# Se le pide al usuario dos numeros
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

# Se compara si n1 es mayor a n2, informar suma y diferencia
if n1 > n2:
    suma = n1 + n2
    diferencia = n1 - n2
    print(f"La suma de los numeros es: {suma}")
    print(f"La diferencia de los numeros es: {diferencia}")

else:
    producto = n1 * n2
    division = n1 / n2
    print(f"El producto de los numeros es: {producto}")
    print(f"La division de los numeros es: {division}")
