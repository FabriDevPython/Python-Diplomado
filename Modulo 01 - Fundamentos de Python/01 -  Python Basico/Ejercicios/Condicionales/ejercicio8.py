"""
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si
dicha fecha corresponde a Navidad.
"""
dia = int(input("Ingrese el numero del dia: "))
mes = int(input("Ingrese el numero del mes: "))
año = int(input("Ingrese el año: "))

if dia == 25 and mes == 12:
    print("Feliz navidad =)")
else:
    print("Todavia no es navidad")