"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y
muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y
muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas
funciones. 
"""
# Función para calcular el cuadrado de un número
def calcular_cuadrado():
    """Solicita un número y muestra su cuadrado."""
    numero = float(input("Ingresa un número para calcular su cuadrado: "))
    cuadrado = numero ** 2
    print(f"El cuadrado es: {cuadrado}")

# ---

# Función para calcular el producto de dos números
def calcular_producto():
    """Solicita dos números y muestra su producto."""
    numero1 = float(input("Ingresa el primer número para la multiplicación: "))
    numero2 = float(input("Ingresa el segundo número para la multiplicación: "))
    producto = numero1 * numero2
    print(f"El producto es: {producto}")

# ---

# Bloque principal del programa
# Aquí es donde se llaman las funciones para que se ejecuten.
calcular_cuadrado()
calcular_producto()