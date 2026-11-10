from string import *


def validar_dni(dni):
    valido = False
    cuentaNum = 0
    cuentaLetra = 0
    
    if(len(dni)>9):
        valido = True
    else :
        valido = False
    
    for caracter in dni:
        if caracter is int:
            cuentaNum = cuentaNum + 1
            numero += str(caracter)
        elif caracter is str:
            cuentaLetra = cuentaLetra + 1
    
    if(cuentaNum==8):
        valido = True
    else :
        valido = False

    if(cuentaLetra==1):
        valido = True
    else :
        valido =False

    resultado = int(str.strip(numero))
    resultado_divison = resultado%23

    cadena =  "TRWAGMYFPDXBNJZSQVHLCKE"
    
    

