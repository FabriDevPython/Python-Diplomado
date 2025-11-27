"""
Variables enteras, flotantes y cadenas de caracteres

Hasta este momento hemos visto como definir variables enteras y flotantes.
Realizar su carga por asignación y por teclado.
Para iniciarlas por asignación utilizamos el operador =.
"""

# Definición de una variable entera
cantidad = 20

# Definición de una variable flotante
altura = 1.92

"""
Como vemos el intérprete de Python diferencia una variable flotante de una variable entera por la
presencia del caracter punto.

Para realizar la carga por teclado utilizando la función input debemos llamar a la
función int o float para convertir el dato devuelto por input:
"""
cantidad = int(input("Ingresar la cantidad de personas: "))

altura = float(input("Ingresar la altura de la persona en metros ej:1.70: "))

"""
A estos dos tipos de datos fundamentales (int y float) se suma un tipo de dato muy
utilizado que son las cadenas de caracteres.

Una cadena de caracteres está compuesta por uno o más caracteres.
También podemos iniciar una cadena de caracteres por asignación o ingresarla por teclado.

Inicialización de una cadena por asignación:
"""
# Definición e inicio de una cadena de caracteres
dia = "lunes"

# Con comillas simples
dia = 'lunes'

"""
Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el
nombre de la persona con mayor altura.
"""
print("Datos de la primer persona")

nombre1 = input("Ingrese nombre: ")
edad1 = int(input("Ingrese la edad: "))
altura1 = float(input("Ingrese la altura Ej 1.75: "))

print("Datos de la segunda persona")

nombre2 = input("Ingrese nombre: ")
edad2 = int(input("Ingrese la edad: "))
altura2 = float(input("Ingrese la altura Ej 1.75: "))

print("La persona mas alta es: ")

if altura1 > altura2:
    print(nombre1)
else:
    print(nombre2)


"""
Realizar la carga de enteros por teclado. Preguntar después que ingresa el
valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.
"""

opcion = "si"
suma = 0

while opcion == "si":
    valor = int(input("Ingrese un valor:"))
    suma = suma + valor
    opcion = input("Desea cargar otro numero (si/no):")

print("La suma de valores ingresados es")
print(suma)



"""
Inicializar un string con la cadena "mAriA" luego llamar a sus métodos upper(), lower() y
capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla.
"""

nombre1 = "mAriA"
print(nombre1)

nombre2 = nombre1.upper() # Todo en mayusculas
print(nombre2)

nombre3 = nombre1.lower() # Todo en minusculas
print(nombre3)

nombre4 = nombre1.capitalize() # Primer caracter en mayusculas
print(nombre4)
