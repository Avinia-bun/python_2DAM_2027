from operaciones_cajero import iniciar_cajero

pin_secreto = 1234
intentos = 3

resultado = iniciar_cajero(pin_secreto,intentos)

if resultado == True:
    print("Acceso Permitido.")
else:
    print("Cuenta bloqueada.")

