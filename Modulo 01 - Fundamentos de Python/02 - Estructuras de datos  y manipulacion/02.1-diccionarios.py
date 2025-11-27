"""
La estructura de datos tipo diccionario utiliza una clave para acceder a un valor.
El subíndice puede ser un entero, un float, un string, una tupla etc.
(en general cualquier tipo de dato inmutable).

• Un diccionario tradicional que conocemos podemos utilizar un diccionario de Python para
representarlo. La clave sería la palabra y el valor sería la definición de dicha palabra.

• Una agenda personal también la podemos representar como un diccionario. La fecha sería la
clave y las actividades de dicha fecha sería el valor. 

• Un conjunto de usuarios de un sitio web podemos almacenarlo en un diccionario. El nombre
de usuario sería la clave y como valor podríamos almacenar su mail, clave, fechas de login
etc.

Recordemos que las listas son mutables y las tuplas inmutables.
Un diccionario es una estructura de datos mutable es decir podemos agregar elementos,
modificar y borrar.

Definición de un diccionario por asignación:
"""


productos = {"manzanas":39, "peras":32, "lechuga":17} # clave: manzanas, valor: 39
print(productos)


"""
En el bloque principal del programa definir un diccionario que almacene los nombres de paises
como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada
clave y valor
"""

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

# bloque principal
paises = {"argentina":40000000, "españa":46000000, "brasil":190000000, "uruguay":
3400000}

imprimir(paises)

"""
Tipos de datos inmutables:

enteros
strings
float
tuplas

Tipos de datos mutables

listas
diccionarios
"""

"""
Porciones de listas, tuplas y cadenas de caracteres.

El lenguaje Python nos facilita una sintaxis muy sencilla par recuperar un trozo
de una lista, tupla o cadena de caracteres.

Veremos con una serie de ejemplos como podemos rescatar uno o varios elementos de las
estructuras de datos mencionadas.
"""
lista1 = [0,1,2,3,4,5,6]

lista2 = lista1[2:5]
print(lista2) # 2,3,4

lista3 = lista1[1:3]
print(lista3) # 1,2

lista4 = lista1[:3]
print(lista4) # 0,1,2

lista5 = lista1[2:]
print(lista5) # 2,3,4,5,6

"""
Indices negativos en listas, tuplas y cadenas de caracteres.

Hemos visto que para acceder a un elemento de una lista, tupla o cadena de caracteres debemos
indicar mediante un subíndice que comienza a numerarse a partir de cero.

También hemos visto el concepto anterior que podemos generar otra lista, tupla o cadena de
caracteres indicando una porción con el caracter ":"

Ahora veremos que podemos utilizar un valor negativo para acceder a un elemento de la estructura
de datos.
"""
lista1 = [0,1,2,3,4,5,6]

print(lista1[-1]) # 6
print(lista1[-2]) # 5