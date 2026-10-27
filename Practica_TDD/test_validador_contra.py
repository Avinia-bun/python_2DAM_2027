from validador_contra import validacion_contrasena

def test_valida_longitud():
    assert validacion_contrasena("Contraseniavalida#1")== True
    assert validacion_contrasena("hola") == False

def test_mayus_validas():
    assert validacion_contrasena("Contraseniavalida#1") == True
    assert validacion_contrasena("hola") == False

def test_minus_validas():
    assert validacion_contrasena("Contraseniavalida#1") == True
    assert validacion_contrasena("MAYUSCULAS") == False

def test_tiene_num():
    assert validacion_contrasena("Contraseniavalida#1") == True
    assert validacion_contrasena("Contrasenianovalida") == False

def test_tiene_especial():
    assert validacion_contrasena("Contraseniavalida1#") == True
    assert validacion_contrasena("Contrasenianovalida1") == False
