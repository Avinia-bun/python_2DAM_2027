from operaciones_cajero import *

def test_verif():
    assert verificar_pin(1234,1234) == True
    assert verificar_pin(1234,5678) == False
    assert verificar_pin(1234,-1234) == False

def test_cajero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1234)
    assert iniciar_cajero(1234,3) == True
    assert iniciar_cajero(5678,3) == False