# Implementa un programa que valide si una contraseña ingresada coincide con la almacenada.

contraAlmacenada = "contraseña123"

print("Bienvenido, usuario.")

contraUsuario = input("Introduce la contraseña: ")

while contraUsuario!=contraAlmacenada:
    print("Error. La contraseña no es correcta.")
    contraUsuario = input("Introduce la contraseña de nuevohol: ")

if contraUsuario==contraAlmacenada:
    print("Contraseña correcta. Entrando al sistema...")