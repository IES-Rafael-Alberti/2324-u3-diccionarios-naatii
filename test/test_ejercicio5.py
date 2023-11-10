from src.ejercicio5 import *
import pytest

@pytest.mark.parametrize(
    "diccionario, expected",
    [
        ({"Matemáticas": 6, "Física": 4, "Química": 5}, 15),
        ({"lengua": 2, "mates": 3, "programación": 5, "ciencia":7}, 17),
    ],
)
def test_totalCreditos(diccionario, expected):
    assert totalCreditos(diccionario) == expected
@pytest.mark.parametrize(
    "cursos, nombre, creditos, expected",
    [
        ({},"Matemáticas", 6, {"Matemáticas":6}),
        ({},"lengua", 2, {"lengua": 2}),
    ]
)
def test_crearCurso(cursos, nombre, creditos, expected):
    assert crearCurso(cursos, nombre, creditos) == expected