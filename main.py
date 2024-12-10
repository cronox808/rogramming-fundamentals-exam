#1. Desarrolle el código fuente de un programa que permita ingresar cinco voltajes, obtener su promedio y 
# visualizar `"ALTO VOLTAJE"`, si su promedio es mayor a 220, caso contrario sea menor mostrar `"VOLTAJE CORRECTO"`.
v1 = int(input("ingrse elvalor del primer voltaje: "))
v2 = int(input("ingrse elvalor del segundo voltaje: "))
v3 = int(input("ingrse elvalor del tercer voltaje: "))
v4 = int(input("ingrse elvalor del cuarto voltaje: "))
v5 = int(input("ingrse elvalor del segundo voltaje: "))

promedio = (v1 + v2 +v3 +v4 +v5) // 5

if(promedio > 220):
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")