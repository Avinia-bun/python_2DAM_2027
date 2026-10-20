numero = input("Introduce el número a invertir: ")

digitos = [int(digito) for digito in numero]
palabra = ""

for i in digitos[::-1]:
    palabra += str(i)
    
print(palabra)