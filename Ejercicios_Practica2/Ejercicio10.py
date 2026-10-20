frase = input("Introduce la frase: ")
contador = 0
for letra in frase:
    if letra.lower() == "a" or  letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
        contador += 1

print("La frase contiene un total de",contador,"vocales.")