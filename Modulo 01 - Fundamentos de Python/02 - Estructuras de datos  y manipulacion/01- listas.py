"""
Las listas son estructuras de datos que se utilizan para almacenar
colecciones ordenadas de elementos. Estos elementos pueden ser
de cualquier tipo, como números, cadenas de caracteres, booleanos
o incluso otras listas.

La funcion len(), cuenta la cantidad de elementos que tiene una lista.
"""
lista_enteros = [10, 5, 3] 
lista_float = [1.78, 2.66, 1.55, 89,4] 
lista_string = ["lunes", "martes", "miercoles"] 
lista_variada = ["juan", 45, 1.92]


# Si queremos conocer la cantidad de elementos de una lista podemos llamar a la función len:
lista_enteros = [10, 5, 3]
print(len(lista_enteros)) # Imprime un 3


# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista = [10, 7, 3, 7, 2]

# Recordemos que tenemos que usar acumuladores para la suma, contadores para las vueltas
suma = 0
x = 0

while x < len(lista):
    suma = suma + lista[x]
    print(suma)
    x += 1

print(f"Los elementos de la lista son: {lista}")
print(f"La suma de todos sus elementos es: {suma}")


# Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año.
# Mostrar el primer y último elemento de la lista solamente.

meses = ["Enero", "Febrero", "Marzo", "Abril"]

print(meses[0])
print(meses[3])


# Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y
# en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

lista = ["Ana", 7, 9]

print(f"Nombre del alumno: {lista[0]}")

promedio = (lista[1] + lista[2]) // 2

print(f"Promedio de sus dos notas: {promedio}")

"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores
almacenan un valor superior a 100.
"""
lista = [1, 2, 3, 100, 80, 20, 70, 200]

contador = 0
superior_100 = 0

while contador < len(lista):
    if lista[contador] >= 100:
        superior_100 += 1
    
    contador += 1

print(superior_100)


"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con
valor iguales o superiores a 7. 
"""
lista = [7, 4, 7, 2, 7]

contador = 0
superior_igual_7 = 0

while contador < len(lista):
    if lista[contador] >= 7:
        superior_igual_7 += 1
    contador += 1

print(superior_igual_7)


"""
Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de
esos nombres tienen 5 o más caracteres. 
"""

lista = ["Fabrizio", "Elian", "Alan", "Nico", "Dillan"]

contador = 0
nombres_5_carac = 0

while contador < len(lista):
    if len(lista[contador]) >= 5:
        nombres_5_carac += 1
    contador += 1

print(nombres_5_carac)


"""
Listas: carga por teclado de sus elementos.

Una lista en Python es una estructura mutable
(es decir puede ir cambiando durante la ejecución del programa)

Una lista luego de definida podemos agregarle nuevos elementos a la colección.
La primera forma que veremos para que nuestra lista crezca es utilizar
el método append que tiene la lista y pasar como parámetro el nuevo elemento:
"""

lista = [10, 20 , 30]
print(len(lista)) # Imprime 3

lista.append(100) # Lo agrega al final de la lista
print(len(lista)) # Imprime 4 / [10, 20, 30, 100]

print(lista[0]) # Imprime 10
print(lista[3]) # Imprime 100

# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado
# y añadirlos a la lista. Imprimir la lista generada.

lista = [] # Lista vacia

for x in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista.append(valor)

print(lista)

# Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []

valor = int(input("Ingresar valor (0 para finalizar): "))

while valor != 0:
    lista.append(valor)
    valor = int(input("Ingresar valor (0 para finalizar): "))

print(f"Tamaño de la lista: {len(lista)}")


"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el
promedio de sueldos.
"""
lista_sueldos = []

for x in range(5):
    sueldo = float(input("Ingrese el sueldo: "))
    lista_sueldos.append(sueldo)

promedio = (lista_sueldos[0] + lista_sueldos[1] + lista_sueldos[2] + lista_sueldos[3] + lista_sueldos[4]) / 5

print(f"La lista de los sueldos es: {lista_sueldos}")
print(f"El promedio de los 5 sueldos es: {promedio}")


"""
Listas: mayor y menor elemento.

Es una actividad muy común la búsqueda del mayor y menor elemento de una lista.
Es necesario que la lista tenga valores del mismo tipo por ejemplo enteros.
Pueden ser de tipo cadenas de caracteres y se busque cual es mayor o menor alfabéticamente,
pero no podemos buscar el mayor o menor si la lista tiene enteros y
cadenas de caracteres al mismo tiempo.
"""

# Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique
# el mayor valor de la lista.

lista = []

for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

mayor = lista[0]

for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]

print(f"Lista completa: {lista}")

print(f"Mayor de la lista: {mayor}")

# Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique
# el menor valor de la lista y la posición donde se encuentra.

lista = []

for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

menor = lista[0]
posicion = 0

for x in range(1,5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x

print(f"Lista completa: {lista}")
print(f"Menor de la lista: {menor}")
print(f"Posicion del menor de la lista: {posicion}")

"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el
nombre de persona menor en orden alfabético. 
"""

lista_nombres = []

# 1. Ingreso de datos
for x in range(5):
    nombre = input("Ingrese nombre: ")
    lista_nombres.append(nombre)


nombre_menor_alfa = lista_nombres[0]

for nombre_actual in lista_nombres:
    if nombre_actual < nombre_menor_alfa:
        nombre_menor_alfa = nombre_actual

# 3. Mostrar el resultado
print("-----------------------------------")
print("La lista ingresada es:", lista_nombres)
print("El nombre menor en orden alfabético es:", nombre_menor_alfa)


"""
Listas paralelas.

Podemos decir que dos listas son paralelas cuando hay una relacion
entre las componentes da igual subindice (misma posicion) de una 
lista y otra.
# -----------------------------------------------
# | nombres | Juan | Ana | Marcos | Pablo | Laura |
# | edades  | 12   | 21  | 27     | 14    | 21    |
# -----------------------------------------------
"""

# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres
# de las personas mayores de edad (mayores o iguales a 18 años)

nombres = []
edades = []

for x in range(5):
    nom = input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed = int(input("Ingrese la edad de la persona: "))
    edades.append(ed)

print("Nombre de las personas mayores de edad: ")

for x in range(5):
    if edades >= 18:
        print(nombres[x])
    


"""
Listas: componentes de tipo lista

Hasta ahora hemos trabajado con listas cuyos componentes son de tipo:
enteros
flotantes
cadenas de caracteres

notas=[8, 6, 8]
alturas=[1.73, 1.55, 1.92]
dias=["lunes", "martes", "miércoles"]

Pero lo que la hace tan flexible a esta estructura de datos es que
podemos almacenar componentes de tipo LISTA

notas = [[4,5], [6,9], [7,3]]

En la línea anterior hemos definido una lista de tres elementos de tipo lista,
el primer elemento de la lista es otra lista de dos elementos de tipo entero.
De forma similar los otros dos elementos de la lista notas son listas de dos
elementos de tipo entero.
"""

# Crear una lista por asignación. La lista tiene que tener cuatro elementos.
# Cada elemento debe ser una lista de 3 enteros.
# Imprimir sus elementos accediendo de diferentes modos.

lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# imprimimos la lista completa
print(lista)
print("---------")

# imprimimos la primer componente
print(lista[0])
print("---------")

# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("---------")

# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
print("---------")

# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])


"""
Listas: eliminación de elementos

Hemos visto que una lista la podemos iniciar por asignación indicando sus elementos.

lista = [10, 20, 30, 40]

También podemos agregarle elementos al final mediante el método append:

lista.append(120)

Otra característica fundamental de las listas en Python es que podemos eliminar
cualquiera de sus componentes llamando al método pop e indicando la posición
del elemento a borrar:

lista.pop(0)

Otra cosa que hay que hacer notar que cuando un elemento de la lista se elimina no queda una
posición vacía, sino se desplazan todos los elementos de la derecha una posición

El método pop retorna el valor almacenado en la lista en la posición indicada,
aparte de borrarlo.

lista = [10, 20, 30, 40]

print(lista.pop(0)) # imprime un 10
"""

lista=[10, 20, 30, 40, 50]
print(lista)
# se imprime [10, 20, 30, 40, 50]

lista.pop(0)
print(lista)
# se imprime [20, 30, 40, 50]

lista.pop(1)
print(lista)
# se imprime [20, 40, 50]

lista.pop(2)
# se imprime [20, 40]
print(lista)


"""
Acotación: otra forma de eliminar elementos de una lista

Para eliminar elementos de una lista también es empleada la función "del"
pasando como parámetro la referencia de la componente a eliminar: 
"""

lista = [10, 20, 30, 40, 50]

print(lista)

del(lista[0])
del(lista[1])
del(lista[2])

print(lista) # 20 40