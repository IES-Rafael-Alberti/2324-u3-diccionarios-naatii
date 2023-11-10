from src.ejercicio7 import crearCarrito, calcularTotal
import pytest
@pytest.mark.parametrize(
    "producto, precio, expected_result", 
    [
        ("Producto1", 10.0, {"Producto1": 10.0}),
        ("Producto2", 11.0, {"Producto2": 11.0}),
        ("Producto3", 20.0, {"Producto3": 20.0})
    ]
)
def test_add_product_to_dictionary(producto, precio, expected_result):
        carrito = {}

        result = crearCarrito(carrito, producto, precio)

        assert result == expected_result
@pytest.mark.parametrize("carrito, expected_total", [
        ({'product1': 10.0, 'product2': 20.0, 'product3': 30.0}, 60.0),
        ({'product1': 5.0, 'product2': 5.0, 'product3': 5.0}, 15.0),
        ({}, 0.0)
    ])
def test_calculate_total_with_valid_dictionary(carrito, expected_total):
        # Act
        result = calcularTotal(carrito)

        # Assert
        assert result == expected_total