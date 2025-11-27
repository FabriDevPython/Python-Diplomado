"""
Confeccionar un programa que lea n pares de datos, cada par de datos
corresponde a la medida de la base y la altura de un triángulo. El programa 
deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.

b) La cantidad de triángulos cuya superficie es mayor a 12.
"""
n = int(input("Ingrese la cantidad de triangulos: "))
triangulos_mayores_a_12 = 0  # Inicializa el contador

for i in range(n):
    print(f"\n--- Triangulo {i + 1} ---") # Mensaje para saber que triangulo estamos calculando
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    
    # a) Calcular la superficie
    superficie = (base * altura) / 2
    
    # a) Mostrar la informacion del triangulo
    print(f"Base: {base}, Altura: {altura}, Superficie: {superficie}")
    
    # b) Contar los triangulos con superficie mayor a 12
    if superficie > 12:
        triangulos_mayores_a_12 += 1

# b) Mostrar el resultado final fuera del ciclo
print("\n--- Resumen ---")
print(f"Cantidad de triangulos con superficie mayor a 12: {triangulos_mayores_a_12}")