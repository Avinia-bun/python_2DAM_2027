from string import *

"""Módulo de validación de identidad y gestión de base de datos."""

def validar_dni(dni):  

    """Valida que un DNI español sea correcto comprobando su longitud, formato numérico y letra de control.
    
    :param dni: Cadena de texto que representa el DNI a validar (debe tener 8 dígitos y 1 letra).
    :type dni: str
    :return: Retorna True si el DNI es totalmente válido.
    :rtype: bool
    :raises ValueError: Si la longitud no es 9, si la parte numérica no es válida, si no termina en letra o si la letra no coincide con el algoritmo oficial.
    """

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
        raise ValueError("La letra del DNI no se corresponde con la que debería tener.")
    else:
        raise ValueError("El DNI debe acabar en una letra.")

def validar_nombre(nombre):
    
    """Valida que un nombre de usuario cumpla con los requisitos de longitud y formato alfabético.

    :param nombre: Cadena de texto con el nombre del usuario.
    :type nombre: str
    :return: Retorna True si el nombre es válido.
    :rtype: bool
    :raises ValueError: Si el nombre excede los 50 caracteres, está vacío, o contiene números/símbolos no alfabéticos.
    """

    if(len(nombre)>50):
        raise ValueError("El nombre tiene más de 50 carácteres.")
    if not nombre:
        raise ValueError("El nombre está vacío.")
    
    if(nombre.isalpha()!=True):
        raise ValueError("El nombre debe contener carácteres alfabéticos únicamente.")
    else:
        return True
    

def guardar_en_bd(dni, nombre, forzar_error = False):

    """Valida el DNI y el nombre, y simula el almacenamiento de los datos en una base de datos.

    :param dni: DNI del usuario a registrar.
    :type dni: str
    :param nombre: Nombre del usuario a registrar.
    :type nombre: str
    :param forzar_error: Bandera opcional para simular un fallo de conexión (por defecto es False).
    :type forzar_error: bool
    :raises ValueError: Si alguna de las funciones de validación de DNI o nombre falla.
    :raises ConnectionError: Si forzar_error se establece en True.
    """

    validar_dni(dni)
    validar_nombre(nombre)

    if(forzar_error==True):
        raise ConnectionError("No se pudo conectar a la base de datos.")
    else:
        print("Usuario con DNI:",dni, "y nombre", nombre, "guardado en BD.")

