from src.ejercicio4 import *
import pytest
@pytest.mark.parametrize(
    "month, expected", 
    [
        (1, "enero"),
        (6, "junio"),
        (12, "diciembre"),
        (13, "")
    ]
)
def test_valid_month_number(month, expected):
        assert calcularMes(month) == expected