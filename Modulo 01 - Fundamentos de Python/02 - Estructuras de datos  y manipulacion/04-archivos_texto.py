"""
Archivos de texto: creación, escritura y lectura.

Una actividad muy común en un programa es el almacenamiento y recuperación de
datos almacenado en un dispositivo secundario (disco duro).

Existen muchos modos de almacenar datos como son los archivos de texto, archivos
binarios, bases de datos etc.

Veremos en este concepto como almacenar y recuperar datos de un archivo de texto.

------------------------------------------------------------------------------------

Archivo de texto

Un archivo de texto contiene un conjunto de caracteres estructurados en distintas
líneas. Es un formato de archivo ampliamente utilizado como pueden ser:

# El código fuente de un script en Python se almacena en un archivo de texto
(igual que cualquier otro lenguaje de programación)

# Archivos HTML, CSS, XML se almacenan en archivos de texto.

# Archivos JSON etc.

----------------------------------------------------------------------------------------

Creación de un archivo de texto y almacenamiento de datos.

Como es una actividad tan común en todo programa el lenguaje Python incluye por
defecto todas las funcionalidades para trabajar con archivos de texto.

Veamos con un ejemplo como crear y almacenar caracteres en un archivo de texto.

---------------------------------------------------------------------------------------------

Crear un archivo de texto llamado 'datos.txt', almacenar tres líneas de texto. Abrir
luego el archivo creado con un editor de texto.
"""
archi1 = open("datos.txt","w") # Crea 'datos.txt' en modo de ESCRITURA ('w').

archi1.write("Primer línea.\n") # Escribe la primera línea. '\n' es el salto de línea.
archi1.write("Segunda línea.\n") # Escribe la segunda línea.
archi1.write("Tercer línea.\n") # Escribe la tercera línea.

archi1.close() # Cierra el archivo. ¡Necesario para guardar los datos en el disco!


"""
Lectura de un archivo de texto.

Leer el contenido del archivo de texto 'datos.txt'.
"""
archi1 = open("datos.txt","r") # Abre el archivo 'datos.txt' en modo de LECTURA ('r').
contenido = archi1.read() # Lee el contenido del archivo y lo almacena en la variable 'contenido'.

print(contenido) # Imprime el contenido leído en la consola.
archi1.close() # Cierra el archivo de lectura.

"""
El método 'read' sin parámetros retorna todos los caracteres almacenados en el
archivo, opcionalmente podemos pasar un entero que represente la cantidad de
caracteres a leer:
"""
archi1 = open("datos.txt", "r")
contenido = archi1.read(6)

print(contenido)
archi1.close()


"""
Lectura de un archivo de texto línea a línea.

En algunas situaciones podemos necesitar leer el contenido de un archivo de texto
línea a línea. Disponemos de un método llamado 'readline' que lee una línea
completa del archivo, inclusive retorna el caracter '\n' de fin de línea.
"""

# Abre el archivo llamado "datos.txt" en modo de lectura ("r").
# El objeto de archivo se asigna a la variable 'archi1'.
archi1 = open("datos.txt","r")

# Lee la primera línea completa del archivo (incluyendo el salto de línea '\n')
# y guarda su contenido en la variable 'linea'.
# Esta es la "lectura previa" esencial para inicializar el bucle 'while'.
linea = archi1.readline()

# Inicia un bucle 'while'. Se repite mientras la variable 'linea' no sea una cadena vacía ('').
# Cuando 'readline()' llega al final del archivo (EOF), devuelve '', y el bucle termina.
while linea != '':
    # Imprime el contenido de la línea actual.
    # El argumento 'end=""' evita que la función 'print' añada su propio salto de línea,
    # ya que 'readline()' ya trajo el salto de línea del archivo original.
    print(linea, end='')
    
    # Lee la siguiente línea del archivo y actualiza la variable 'linea'.
    # Esto es crucial para dos cosas: 
    # 1. Obtener la próxima línea a procesar.
    # 2. Controlar la condición del bucle 'while' (evitar bucle infinito).
    linea=archi1.readline()

# Cierra explícitamente el archivo para liberar los recursos del sistema.
# Esta es una buena práctica para asegurar que todas las operaciones de I/O finalicen correctamente.
archi1.close()

"""
Podemos recorrer el archivo leyendo línea a línea utilizando la estructura repetitiva
for:
"""

archi1 = open("datos.txt","r")

for linea in archi1:
    print(linea, end='')

archi1.close()

"""
Almacenar un archivo de texto en una lista.

Mediante el método 'readlines' podemos recuperar cada una de las líneas del archivo
de texto y almacenarlas en una lista.

Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista.
Imprimir la cantidad de líneas que tiene el archivo y su contenido.
"""
archi1 = open("datos.txt","r")
lineas = archi1.readlines()

print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')

for linea in lineas:
    print(linea, end='')

archi1.close()

