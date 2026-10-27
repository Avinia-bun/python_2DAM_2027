import string

def validacion_contrasena(contra):
    long_valida = len(contra)>=8
    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False
    tiene_especial = False
    for caracter in contra:
        if caracter.isupper():
            tiene_mayus = True
        elif caracter.islower() :
            tiene_minus = True
        elif caracter.isdigit():
             tiene_numero = True
        elif caracter in string.punctuation:
            tiene_especial = True
    return long_valida & tiene_mayus & tiene_minus & tiene_numero & tiene_especial
        