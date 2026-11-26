from algoritmos import generar_datos
from algoritmos import tiene_duplicados_lento
from algoritmos import tiene_duplicados_rapido

import timeit

n = 3
print("Cada algoritmo se repetirá 3 veces.")
print("Resultados para 5.000 de entrada: ")

tiempo_len = timeit.timeit(lambda : tiene_duplicados_lento(generar_datos(5000)), number=n)
tiempo_rap = timeit.timeit(lambda : tiene_duplicados_rapido(generar_datos(5000)), number=n)

print(f"Resultados de la función lenta: {tiempo_len:.6f}")
print(f"Resultados de la función rápida: {tiempo_rap:.6f}")

# print("Resultados para 15.000 de entrada: ")

# tiempo_len = timeit.timeit(lambda : tiene_duplicados_lento(generar_datos(15000)), number=n)
# tiempo_rap = timeit.timeit(lambda : tiene_duplicados_rapido(generar_datos(15000)), number=n)

# print(f"Resultados de la función lenta: {tiempo_len:.6f}")
# print(f"Resultados de la función rápida: {tiempo_rap:.6f}")

# print("Resultados para 30.000 de entrada: ")

# tiempo_len = timeit.timeit(lambda : tiene_duplicados_lento(generar_datos(30000)), number=n)
# tiempo_rap = timeit.timeit(lambda : tiene_duplicados_rapido(generar_datos(30000)), number=n)

# print(f"Resultados de la función lenta: {tiempo_len:.6f}")
# print(f"Resultados de la función rápida: {tiempo_rap:.6f}")

# print("Resultados para 50.000 de entrada: ")

# tiempo_len = timeit.timeit(lambda : tiene_duplicados_lento(generar_datos(50000)), number=n)
# tiempo_rap = timeit.timeit(lambda : tiene_duplicados_rapido(generar_datos(50000)), number=n)

# print(f"Resultados de la función lenta: {tiempo_len:.6f}")
# print(f"Resultados de la función rápida: {tiempo_rap:.6f}")