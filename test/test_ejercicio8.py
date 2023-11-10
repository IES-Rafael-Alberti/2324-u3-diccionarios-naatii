from src.ejercicio8 import *
import pytest
def test_traducir():
    diccionario = {"hola": "hello", "adios": "goodbye"}
    cadena = ["hola", "adios"]
    assert traducir(diccionario, cadena) == "hello goodbye "
@pytest.mark.parametrize(
    "diccionario, significado, expected", 
    [
        ({'hola': 'hello'}, ['adios', 'goodbye'], {'hola': 'hello', 'adios': 'goodbye'})
    ]
)
def test_crearDiccionario(diccionario, significado, expected):
    result = crearDiccionario(diccionario, significado)
    assert result == expected