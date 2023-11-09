from src.ejercicio6 import *
import pytest


@pytest.mark.parametrize(
    "diccionarioUsuarios, usuarios, nombre, edad, sexo, telefono, correo, expected",
    [
        (
            {},0,"natalia",25,"mujer",1234567890,"natalia@example.com",{"usuario0": ["natalia", 25, "mujer", 1234567890, "natalia@example.com"]},
        ),
        ({}, 1, "marta", 12, "mujer", 1234567890, "marta@example.com", {"usuario1": ["marta", 12, "mujer", 1234567890, "marta@example.com"]}),
        ({}, 2, "pedro", 34, "hombre", 1234567890, "pedro@example.com", {"usuario2": ["pedro", 34, "hombre", 1234567890, "pedro@example.com"]}),
        ({}, 3, "roberto", 34, "hombre", 1234567890, "roberto@example.com", {"usuario3": ["roberto", 34, "hombre", 1234567890, "roberto@example.com"]}),
    ],
)
def test_receives_dictionary_integer_and_strings(diccionarioUsuarios, usuarios, nombre, edad, sexo, telefono, correo, expected):
    assert crearDiccionarioUsuarios(diccionarioUsuarios, usuarios, nombre, edad, sexo, telefono, correo) == expected
