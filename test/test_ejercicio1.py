from src.ejercicio1 import *
import pytest

@pytest.mark.parametrize(
    "divisa, diccionarioDivisas, resultado",
    [
        ("Euro", {"Euro":"€", "Dollar":"$", "Yen":"¥"}, True),
        ("Dollar", {"Euro":"€", "Dollar":"$", "Yen":"¥"}, True),
        ("Yen", {"Euro":"€", "Dollar":"$", "Yen":"¥"}, True),
        ("euro", {"Euro":"€", "Dollar":"$", "Yen":"¥"}, True),
        ("centavos", {"Euro":"€", "Dollar":"$", "Yen":"¥"}, False),
    ]
)
def test_detectar_divisa(divisa, diccionarioDivisas, resultado):
    assert detectarDivisa(divisa, diccionarioDivisas) == resultado