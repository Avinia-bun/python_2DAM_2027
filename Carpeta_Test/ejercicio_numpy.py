import numpy as np

numeros = np.array([1, 2, 3, 4, 5])

print("Array:", numeros)
print("Suma:", np.sum(numeros))
print("Media:", np.mean(numeros))

#En python no se usan llaves, todo se basa en la indentación. Define qué se ejecuta y qué no.
if True:
    print("Parte del if")
else:
    print("Parte del else")
print("Fuera del if")