"""
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la
siguiente información: cantidad total de preguntas que se le realizaron y la
cantidad de preguntas que contestó correctamente. Se pide confeccionar un
programa que ingrese los dos datos por teclado e informe el nivel del mismo
según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:

Nivel maximo: Porcentaje >= 90%
Nivel medio: Porcentaje >= 75% y 90%
Nivel regular: Porcentaje >= 50% y 75%
Fuera de nivel: Porcentaje < 50%
"""

total_preguntas = int(input("¿Cuantas preguntas le realizaron? "))
preguntas_correctas = int(input("¿Cuantas preguntas respondio correctamente? "))

porcentaje = (preguntas_correctas / total_preguntas) * 100
print(f"Su porcentaje es: {porcentaje}%")

if porcentaje >= 90:
    print("Nivel maximo.")
else:
    # Si no es Nivel maximo, el porcentaje es menor a 90%
    if porcentaje >= 75:
        print("Nivel medio.")
    else:
        # Si no es Nivel medio, el porcentaje es menor a 75%
        if porcentaje >= 50:
            print("Nivel regular.")
        else:
            # Si ninguna de las condiciones anteriores se cumple, el porcentaje es menor a 50%
            print("Fuera de nivel.")