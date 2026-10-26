def validacion_contrasena(contra):
    long_valida = len(contra)>=8
    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False
    for caracter in contra:
        if caracter.isupper():
            tiene_mayus = True
        if caracter.islower() :
            tiene_minus = True
        if caracter.isdigit():
             tiene_numero = True
        if
    return long_valida & tiene_mayus & tiene_minus & tiene_numero
        