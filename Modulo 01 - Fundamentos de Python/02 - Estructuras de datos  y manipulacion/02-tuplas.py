"""
Una tupla permite almacenar una colección de datos no necesariamente del mismo tipo.

Los datos de la tupla son inmutables a diferencia de las listas que son mutables.

Una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos.
La sintaxis para definir una tupla es indicar entre paréntesis sus valores:
"""
tupla = (1, 2, 3)
fecha = (25, "Diciembre", 2016)
punto = (10, 2)
persona = ("Rodriguez", "Pablo", 43)

print(tupla)
print(fecha)
print(punto)
print(persona)

"""
Podemos acceder a los elementos de una tupla en forma similar
a una lista por medio de un subíndice:
"""
print(punto[0]) # primer elemento de la tupla
print(punto[1]) # segundo elemento de la tupla

"""
Conversión de tuplas a listas y viceversa.

Otra herramienta que nos proporciona Python es la conversión de tuplas a listas y viceversa
mediante las funciones:

list(parametro de tipo tupla)
tuple(parametro de tipo lista)
"""
fechatupla1 = (25, 9, 2025)

print("Imprimimos la primer tupla")
print(fechatupla1)

fechalista = list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0] = 31

print("Imprimimos la lista ya modificada")
print(fechalista)

fechatupla2 = tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)


"""
Empaquetado y desempaquetado de tuplas.

Podemos generar una tupla asignando a una variable un conjunto
de variables o valores separados por coma:
"""
# Empaquetar
x = 10
y = 30

punto = x,y

print(punto)
print(type(punto))

# Desempaquetar
fecha=(25, "diciembre", 2016)
print(fecha)

dd,mm,aa = fecha
print("Dia" ,dd)
print("Mes" ,mm)
print("Año" ,aa)


"""
Listas y tuplas anidadas

La lista es una estructura mutable (es decir podemos modificar sus elementos,
agregar y borrar) en cambio una tupla es una secuencia de datos inmutable,
es decir una vez definida no puede cambiar.

En Python vimos que podemos definir elementos de una lista que sean de tipo lista,
en ese caso decimos que tenemos una lista anidada.

Ahora que vimos tuplas también podemos crear tuplas anidadas.

En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa,
es decir listas con componente tipo tupla.
"""

empleado = ["juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)

print("----------------")

alumno = ("pedro",[7, 9])
print(alumno)

alumno[1].append(10)
print(alumno)

"""
Variantes de la estructura repetitiva for para recorrer tuplas y listas.

Hasta ahora siempre que recorremos una lista o una tupla utilizando
un for procedemos de la siguiente manera:
"""
lista = [2, 3, 50, 7, 9]

for x in range(len(lista)):
    print(lista[x])


"""
Esta forma de recorrer la lista es utilizada obligatoriamente cuando
queremos modificar sus elementos como podría ser:
"""

lista = [2, 3, 50, 7, 9]
print(lista) # [2, 3, 50, 7, 9]

for x in range(len(lista)):
    if lista[x]<10:
        lista[x] = 0

print(lista)


"""
Ahora veremos una segunda forma de acceder a los elementos de una lista con la estructura
repetitiva for sin indicar subíndices.
"""
lista = [2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)


tupla = (2, 3, 50, 7, 9)


for elemento in tupla:
    print(elemento)


"""
Como podemos ver la instrucción for requiere una variable (en este ejemplo llamada elemento),
luego la palabra clave in y por último el nombre de la lista. El bloque del for se ejecuta
tantas veces como elementos tenga la lista, y en cada vuelta del for la variable elemento
almacena un valor de la lista.
"""


