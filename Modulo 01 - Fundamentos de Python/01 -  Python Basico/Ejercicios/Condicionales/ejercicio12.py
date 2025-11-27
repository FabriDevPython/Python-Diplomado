"""
Escribir un programa que pida ingresar la coordenada de un punto en el
plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""
x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

if x > 0 and y > 0:
    print("1° Cuadrante.")
else:
    print("2° Cuadrante.")