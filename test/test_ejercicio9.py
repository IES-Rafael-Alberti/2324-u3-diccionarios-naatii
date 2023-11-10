from src.ejercicio9 import *
import pytest

@pytest.mark.parametrize(
        "diccionario, factura, costoFactura, expected", 
    [
        ({}, 123, 100.0, {123: 100.0})
    ]
)
def test_empty_dictionary(diccionario, factura, costoFactura, expected):
    result = crearDiccionarioFacturas(diccionario, factura, costoFactura)
    assert result == expected
@pytest.mark.parametrize("diccionario, factura", [({1: 10, 2: 20, 3: 30}, 2)])
def test_present_factura(diccionario, factura):
    assert pagar(diccionario, factura) == True