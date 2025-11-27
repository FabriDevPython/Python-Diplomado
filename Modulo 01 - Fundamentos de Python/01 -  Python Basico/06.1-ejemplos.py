"""
Ejemplos de problemas que capturan excepciones.
Problema:
Realizar la carga de dos números por teclado e imprimir la división del primero
respecto al segundo, capturar la excepción ZeroDivisionError.
"""
try:
    valor1 = int(input("Ingrese dividendo:"))
    valor2 = int(input("Ingrese divisor:"))
    division = valor1 / valor2
    print("El resultado de la división es", division)

except ZeroDivisionError:
    print("No se puede dividir por cero.")

"""
Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del
número de mes y mostrar seguidamente el nombre de dicho mes. Capturar la
excepción IndexError.
"""
meses = ("enero" ,"febrero" ,"marzo" ,"abril" ,"mayo" ,"junio" ,
"julio" ,"agosto" ,"septiembre" ,"octubre" ,"noviembre" ,"diciembre")

try:
    num_mes = int(input("Ingrese un número de mes [1-12]:"))
    print(meses[num_mes -1])

except IndexError:
    print("En número de mes debe ir entre 1 y 12")


"""
Realizar la carga de dos números por teclado e imprimir la división del primero
respecto al segundo, capturar las excepciones ZeroDivisionError y ValueError.
"""
try:
    valor1 = int(input("Ingrese dividendo:"))
    valor2 = int(input("Ingrese divisor:"))
    division = valor1 / valor2
    print("El resultado de la división es", division)

except ZeroDivisionError:
    print("No se puede dividir por cero.")

except ValueError:
    print("Los valores a ingresar deben ser enteros")

"""
Realizar la carga de dos números por teclado e imprimir la división del primero
respecto al segundo. Capturar cualquier tipo de excepción que se dispare.
"""
try:
    valor1 = int(input("Ingrese dividendo:"))
    valor2 = int(input("Ingrese divisor:"))
    division = valor1 / valor2
    print("El resultado de la división es", division)

except:
    print("Problemas con la entrada u operacion")

