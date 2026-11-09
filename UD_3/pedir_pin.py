pin = 1234
num  = 0
intentos = 3

while intentos > 0 and num != pin:
    num = int(input("Introduce el PIN: "))
    if num == pin:
        print("Acceso permitido.")
    else:
        print("Pin incorrecto.") 
        intentos = intentos -1

if intentos == 0:
    print("Cuenta bloqueada.")
