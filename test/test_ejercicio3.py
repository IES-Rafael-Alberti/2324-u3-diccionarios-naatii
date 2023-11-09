from src.ejercicio3 import *
import pytest
@pytest.mark.parametrize("fruta, kilos, expected", [
        ('platano', 2, 2.7),
        ('manzana', 1.5, 1.2),
        ('pera', 1, 0.85),
        ('naranja', 3, 2.1),
        ('fresa', 1, 0)
    ])
def test_calcularPrecio(fruta, kilos, expected):
        assert calcularPrecio(fruta, kilos) == expected