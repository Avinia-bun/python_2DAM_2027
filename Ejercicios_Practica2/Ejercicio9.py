import random

numero = random.randint(1,100)

numUser = int(input("Introduce un número: "))

while numUser!=numero:
    print("Has fallado.")
    if numUser>numero:
        print("El número secreto es menor.")
    else:
        print("El numero secreto es mayor.")
    numUser = int(input("Vuelve a intentarlo: "))

print("Enhorabuena! Has acertado!")