# Elabora un algoritmo que calcule el promedio de tres notas y muestre si el estudiante aprueba.

nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))

promedio = (nota1+nota2+nota3)/3

if promedio<5:
    print("Has suspendido. Tu promedio es ", promedio)
else:
    print("Has aprobado. Tu promedio es ", promedio)