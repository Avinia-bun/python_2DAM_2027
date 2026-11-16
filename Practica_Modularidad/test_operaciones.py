from operaciones import *
import pytest

def test_validar_dni():
    assert validar_dni("12345678Z") == True

    with pytest.raises(ValueError, match="La letra del DNI no se corresponde con la que debería tener."):
        validar_dni("12345678A")

    with pytest.raises(ValueError, match="El DNI no cumple la longitud necesaria"):
        validar_dni("1")

    with pytest.raises(ValueError, match="El DNI debe estar compuesto por 8 números seguidos de una letra."):
        validar_dni("123456789")

def test_validar_nombre():
    validar_nombre("Ana") == True

    with pytest.raises(ValueError, match="El nombre está vacío o tiene más de 50 carácteres."):
        validar_nombre("")
        validar_nombre("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    with pytest.raises(ValueError, match="El nombre debe contener carácteres alfabéticos únicamente."):
        validar_nombre("Lu1s")


def test_guardar_en_bd():
    with pytest.raises(ConnectionError, match="No se pudo conectar a la base de datos."):
        guardar_en_bd("12345678Z","María", True)

        

