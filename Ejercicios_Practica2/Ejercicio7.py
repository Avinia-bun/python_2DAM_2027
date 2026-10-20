numero = int(input("Introduce un número negativo o positivo: "))
contador = 0

while numero>=0:
    numero = int(input("Introduce el siguiente: "))
    contador += 1

print("Total de números positivos introducidos:",contador)