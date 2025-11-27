"""
De un operario se conoce su sueldo y los años de antigüedad. Se pide
confeccionar un programa que lea los datos de entrada e informe:

a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
otorgarle un aumento del 20 %, mostrar el sueldo a pagar.

b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
otorgarle un aumento de 5 %.

c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
cambios.
"""

sueldo = int(input("Ingrese su sueldo: "))
antiguedad = int(input("Ingrese sus años de antiguedad: "))

if sueldo < 500 and antiguedad >= 10:
    print(f"Su sueldo es de: ${sueldo}, aumenta un 20%")
    aumento_20 = (sueldo * 0.2) + sueldo
    print(f"Su sueldo ahora es de: ${aumento_20}")

elif sueldo < 500 and antiguedad < 10:
    print(f"Su sueldo es de: ${sueldo}, aumenta un 5%")
    aumento_5 = (sueldo * 0.05) + sueldo
    print(f"Su sueldo es de: ${aumento_5}")

else:
    sueldo >= 500
    print(f"Su sueldo es de: ${sueldo}, no recibe aumento")