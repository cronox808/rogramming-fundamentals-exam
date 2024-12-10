import math

a = float(input("ingrese el valor de los lados del triangulo eqilatero: "))

raiz = (math.sqrt(3)/4) * (a** 2)

if(raiz >= 1000):
    print("DATOS NO VÁLIDOS")
else:
    print(f"el area del triangulo es {raiz}")