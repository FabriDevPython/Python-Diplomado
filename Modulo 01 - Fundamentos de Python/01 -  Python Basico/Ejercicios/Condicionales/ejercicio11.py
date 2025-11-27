"""
Se ingresan tres valores por teclado, si todos son iguales se imprime la suma
del primero con el segundo y a este resultado se lo multiplica por el tercero.
"""
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

if n1 == n2 and n2 == n1:
    resultado = (n1 + n2) * n3
    print(resultado)
else:
    print("Los valores no son todos iguales.")