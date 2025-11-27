"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el
número es positivo, negativo o nulo (es decir cero)
"""
n1 = int(input("Ingrese un numero: "))

if n1 >= 0:
    # Si n1 es mayor o igual a cero, puede ser positivo o nulo
    if n1 == 0:
        print("El número es nulo (cero).")
    else:
        print("El número es positivo.")
else:
    # Si la primera condición es falsa, el número debe ser negativo
    print("El número es negativo.")