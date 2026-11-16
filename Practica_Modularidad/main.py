from operaciones import *

dni = input("Introduce el DNI: ")
try:
    validar_dni(dni)
except  ValueError:
   print("DNI inválido.")

nombre = input("Intoduce el nombre: ")
try:
    validar_nombre(nombre)
except ValueError:
    print("Nombre inválido.")


try:
    guardar_en_bd(dni, nombre, False)
except ConnectionError:
    print("Error al conectar.")
