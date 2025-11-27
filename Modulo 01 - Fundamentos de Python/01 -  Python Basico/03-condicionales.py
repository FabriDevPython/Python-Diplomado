"""
Los condicionales son estructuras de control de flujo que permiten
tomar decisiones en función del valor de una expresión booleana.
"""
# Estructura simple
sueldo = int(input("Ingrese cual es su sueldo: "))
if sueldo > 3000:
    print("Esta persona debe abonar impuestos")


# Estructura compuesta
num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))

print("El valor mayor es: ")

if num1 > num2:
    print(num1)
else:
    print(num2)


# Estructura anidada
nota1 = int(input("Ingrese primer nota :"))
nota2 = int(input("Ingrese segunda nota :"))
nota3 = int(input("Ingrese tercer nota :"))
prom = (nota1 + nota2 + nota3) / 3

if prom >= 7:
    print("Promocionado")
else:
    if prom >= 4:
        print("Regular")
    else:
        print("Reprobado")



num1 = int(input("Ingrese primer valor :"))
num2 = int(input("Ingrese segundo valor :"))
num3 = int(input("Ingrese tercer valor :"))
print("El mayor de los tres valores es")

if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)


dia = int(input("Ingrese nro de día:"))
mes = int(input("Ingrese nro de mes:"))
año = int(input("Ingrese nro de año:"))

if mes == 1 or mes == 2 or mes == 3:
    print("Corresponde al primer trimestre")


dd = int(input("Ingrese nro de día:"))
mm = int(input("Ingrese nro de mes:"))
aa = int(input("Ingrese nro de año:"))

if mm == 12 and dd == 25:
    print("La fecha ingresada corresponde a navidad.")
