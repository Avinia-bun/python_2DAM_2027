from string import *


def validar_dni(dni):  
    if(len(dni)!=9):
        raise ValueError("El DNI no cumple la longitud necesaria")
       
    try:
        numero = int(dni[-9:-1])
    except ValueError:
        raise ValueError("El DNI debe estar compuesto por 8 números seguidos de una letra.")
    
    letra = dni[-1]
    
    if letra.isalpha():
        idx = numero % 23
        cadena = "TRWAGMYFPDXBNJZSQVHLCKE"
        if(cadena[idx] == letra):
            return True
        else:
            raise ValueError("La letra del DNI no se corresponde con la que debería tener.")


def validar_nombre(nombre):
    
    if(len(nombre)>50 or nombre is None):
        raise ValueError("El nombre está vacío o tiene más de 50 carácteres.")
    
    if(nombre.isalpha()!=True):
        raise ValueError("El nombre debe contener carácteres alfabéticos únicamente.")
    else:
        return True
    

def guardar_en_bd(dni, nombre, forzar_error = False):

    validar_dni(dni)
    validar_nombre(nombre)

    if(forzar_error==True):
        raise ConnectionError("No se pudo conectar a la base de datos.")
    else:
        print("Usuario con DNI: {dni} y nombre {nombre} guardado en BD.")

