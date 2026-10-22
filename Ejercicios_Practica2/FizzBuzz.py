# Las reglas del juego: recorres los números del 1 al N. Si el número es múltiplo de 3 escribes «Fizz»; fizz entre 3 buzz entre 5 bizzbuzz entre 3 y 5
# si es múltiplo de 5, «Buzz»; si es múltiplo de ambos, «FizzBuzz»; 
# y si no es múltiplo de ninguno, escribes el número. 
# Vas a ver la solución principal con Si anidados, dos variantes (condición con Y y construcción de la palabra con Concatenar), 
# la prueba de escritorio del 1 al 15 y los errores que más puntos cuestan. ¿Empezamos?

for i in range(1,101): 
    if i%3 == 0 and i%5!=0 :
        print("Fizz")
    elif i%3!=0 and i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)
    