"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y
$500, realizar un programa que lea los sueldos que cobra cada empleado e
informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más
de $300. Además el programa deberá informar el importe que gasta la
empresa en sueldos al personal
"""
n = int(input("¿Cuantos empleados trabajan en tu empresa? "))

contador = 1

sueldo_entre_100_300 = 0

sueldo_mas_300 = 0

gastos = 0

while contador <= n:
    sueldo = int(input("Ingrese su sueldo: "))
    contador += 1

    if sueldo <= 300:
         sueldo_entre_100_300 += 1
    else:
         sueldo_mas_300 += 1
        
    gastos = gastos + sueldo


print(f"Los empleados que cobran entre $100 y $300 son: {sueldo_entre_100_300}")
print(f"Los empleados que cobran mas de $300 son: {sueldo_mas_300}")

print(f"Los gastos de la empresa en sueldos es de: ${gastos}")
