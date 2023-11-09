from src.ejercicio2 import *
import pytest

@pytest.mark.parametrize(
    "nombre,edad,direccion, telefono, expected",
    [
        ("John", 25, "123 Main St", 1234567890, {'nombre': 'John', 'edad': 25, 'direccion': '123 Main St', 'telefono': 1234567890}),
        ("Jane", 25, "123 Main St", 1234567890, {'nombre': 'Jane', 'edad': 25, 'direccion': '123 Main St', 'telefono': 1234567890}),
    ]
)
def test_registroUsuario(nombre, edad, direccion, telefono, expected):
    assert registroUsuario(nombre, edad, direccion, telefono) == expected