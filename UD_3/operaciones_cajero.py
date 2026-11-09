def pedir_pin():
    while True:
        num = input("Introduce el pin: ")
        try:
            int(num)
            return num
        except  ValueError:
            print("Error. No se ha introducido un número. Intente de nuevo")

def verificar_pin(pin,num):
    if num == pin:
        return True
    else:
        return False
    
def iniciar_cajero(pin, intentos):
    while intentos > 0:
        numero = pedir_pin()
        pin_secreto = pin
        resultado = verificar_pin(pin_secreto,numero)
        if resultado == True:
            print("PIN correcto.")
            return True
        else:
            print("Pin incorrecto.")
            intentos -= 1
            print("Intentos restantes: ",intentos)

    if intentos == 0:
        return False
