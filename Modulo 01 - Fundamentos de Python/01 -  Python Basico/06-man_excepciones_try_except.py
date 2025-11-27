"""
Las excepciones son errores que se disparan durante la ejecución de un programa.
En Python podemos dejar que dichas excepciones detengan el programa o en caso
contrario escribir un algoritmo para reaccionar a dicha situación.

Los ejemplos más comunes que podemos nombrar de excepciones:

•Tratar de convertir a entero un string que no contiene valores numéricos.

•Tratar de dividir por cero.

•Abrir un archivo de texto inexistente o que se encuentra bloqueado por otra
aplicación.

•Conectar con un servidor de bases de datos que no se encuentra activo.

•Acceder a subíndices de listas o tuplas inexistentes.

•Llamada a un método o función inexistente.

•Importar módulos que no existen.

--------------------------------------------------------------

ValueError: Se genera cuando una operación o función recibe un argumento
que tiene un valor inapropiado como vimos en el concepto anterior al tratar de
convertir un string a entero siendo que el string no contiene valores
numéricos
"""
while True:
    try:
        valor1 = int(input("Ingrese primer valor: "))
        valor2 = int(input("Ingrese segundo valor: "))
        
        suma = valor1 + valor2
        print(f"La suma es: {suma}")
    
    except ValueError:
        print("Debe ingresar numeros.")
    
    respuesta = input("Desea ingresar otro par de valores?[s/n]")
    if respuesta == "n":
        break

########################################################################

"""
IndexError: Se genera cuando un subíndice de una secuencia (tupla, lista,
string) está fuera de rango. Por ejemplo en una lista de 5 elementos queremos
acceder al elemento con subíndice 70.
"""
lista = [1, 2, 3, 4, 5]
print(lista[70])

###########################################################################

"""
NameError: Se genera cuando llamamos a una función, método o tratamos
de acceder a una variable inexistente.
"""
print(x)

################################################################################

"""
TypeError: Se genera cuando una operación o función se aplica a un tipo de
dato inapropiado. Por ejemplo si queremos sumar un entero y un string:
"""
suma = 10 + "juan"
print(suma)

##################################################################################

"""
ModuleNotFoundError: Se genera cuando la declaración de un import tiene
problemas al intentar cargar el módulo inexistente:
"""
import randomx

##################################################################################

"""
ZeroDivisionError: Se genera cuando intentamos dividir una variable o valor
por cero:
"""
cantidad = 0
total = 100 / cantidad
print(total)

#####################################################################################

"""
OverflowError: Se genera cuando un resultado de una operación aritmética
con valores reales (no enteros) es demasiado grande para ser representado:
"""
resultado = 5.25 ** 25665

####################################################################################

"""
KeyError: Se genera cuando no se encuentra una clave en un diccionario:
"""
productos = {
    "manzanas" : 39,
    "peras" : 32,
    "lechugas" : 17

}

print(productos["sandias"])

