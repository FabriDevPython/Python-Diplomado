"""
Hemos visto que la sintaxis para la captura de excepciones es:

try:
    [algoritmo principal]

except [nombre de la excepción 1]:
    [algoritmo alternativo 1]


except [nombre de la excepción 2]:
    [algoritmo alternativo 2]

except [nombre de la excepción 3]:
    [algoritmo alternativo 3]

---------------------------------------------------------------------
Hay otra sección opcional de la cláusula 'try' llamada 'finally':

try:
    [algoritmo principal]

except [nombre de la excepción 1]:
    [algoritmo alternativo 1]


except [nombre de la excepción 2]:
    [algoritmo alternativo 2]

except [nombre de la excepción 3]:
    [algoritmo alternativo 3]

finally:
    [algoritmo que siempre se ejecuta]

---------------------------------------------------------------------
Cuando en el algoritmo principal se genera una excepción las instrucciones que
continúan nunca se ejecutarán ya que pasa a ejecutar el bloque del 'except'. Hay
situaciones donde queremos que haya un algoritmo que siempre se ejecute ya sea
que se dispare una excepción o no.

Veamos algunos ejemplos donde es conveniente emplear el bloque finally.
-------------------------------------------------------------------------
Problema:

Almacenar una serie de string en un archivo de texto. Tratar de llamar al método
'write' pasando un entero.
"""
try:
    archi1=open("datos.txt","w")
    archi1.write("Primer línea.\n")
    archi1.write("Segunda línea.\n")
    archi1.write("Tercer línea.\n")
    archi1.write(3334)

except TypeError:
    print("No se puede grabar un entero con write")

finally:
    archi1.close()
    print("Se cerró el archivo")

 