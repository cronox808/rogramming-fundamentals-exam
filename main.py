v1 = float(input("ingrese el primer voltaje: "))
v2 = float(input("ingrese el segundo voltaje: "))
v3 = float(input("ingrese el tercero voltaje: "))

promedio = v1 + v2 + v3 // 3

if(promedio < 150):
    print("VOLTAJE CORRECTO")
elif(promedio > 150 and promedio < 220):
    print("ALTO VOLTAJE")
elif(promedio > 220):
    print("PELIGRO")