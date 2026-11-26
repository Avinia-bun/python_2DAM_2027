from algoritmos import generar_datos
from algoritmos import tiene_duplicados_lento
from algoritmos import tiene_duplicados_rapido

def test_algoritmos_duplicados():
    assert tiene_duplicados_rapido(generar_datos(5)) == True
    assert tiene_duplicados_lento(generar_datos(5)) == True

def test_algoritmos_no_duplicados():
    assert tiene_duplicados_rapido(generar_datos(1)) == False
    assert tiene_duplicados_lento(generar_datos(1)) == False