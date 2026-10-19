segundos = input("Hola! Introduce los segundos que deseas convertir")
valido = False


while valido == False:

    try:
        numero = float(segundos)
        valido=True
        break
    except ValueError:
        print("Error: No se ha introducido un dato válido.")

