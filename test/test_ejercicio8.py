from src.ejercicio8 import *

def test_traducir():
    diccionario = {"hola": "hello", "adios": "goodbye"}
    cadena = ["hola", "adios"]
    assert traducir(diccionario, cadena) == "hello goodbye "