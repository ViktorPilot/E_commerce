from typing import Any
from unittest.mock import Mock, patch

from src.product import Product


def test_init_product_valid(product_casio: Product) -> None:
    """Тестирование создания экземпляра класса 'Product' при валидных значениях"""
    assert product_casio.name == "casio"
    assert product_casio.description == "for_current_time"
    assert product_casio.price == 100.00
    assert product_casio.quantity == 4


def test_new_product(product_casio: Product) -> None:
    """Тестирование классметода, позволяющего создать объект класса 'Product',
    суммирущего общее количество и выбирающего максимальную цену товара при наличии товаров с тем же названием"""
    product2 = Product.new_product({"name": "casio", "description": "for_current_time", "price": 80.00, "quantity": 8})
    assert product2.name == "casio"
    assert product2.price == 100.00
    assert product2.quantity == 12


def test_price_getter(product_casio: Product) -> None:
    """Тестирование геттера класса 'Product', позволяющего вызвать цену товара с приватным уровнем доступа"""
    assert product_casio.price == 100.00


@patch("builtins.input")
def test_price_setter(mock_input: Mock, capsys: Any, product_casio: Product) -> None:
    """Тестирование сеттера класса 'Product', позволяющего изменять цену товара с приватным уровнем доступа"""

    # при новой цене больше 0 и больше старого значения
    product_casio.price = 200.00
    assert product_casio.price == 200.00

    # при новой цене меньше 0
    product_casio.price = -100.00
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product_casio.price == 200.00

    # при новой цене больше 0, но меньше старого значения
    # при выборе пользователя - изменить старое значение цены на новое
    mock_input.return_value = "y"
    product_casio.price = 50.00
    assert product_casio.price == 50.00

    # при новой цене больше 0, но меньше старого значения
    # при выборе пользователя - не изменять старое значение цены на новое
    mock_input.return_value = "n"
    product_casio.price = 30.00
    assert product_casio.price == 50.00

    # при вводе неверного ответа при первой попытке
    product_casio.price = 50.00
    mock_input.side_effect = ["a", "y"]
    assert product_casio.price == 50.00

def test_str_product(product_casio: Product) -> None:
    """Тестирование магического метода __str__, возвращающего информацию о продукте"""
    assert str(product_casio) == "casio, 100.0 руб. Остаток: 4 шт."

def test_add_product(product_casio: Product, add_product1: Product) -> None:
    """Тестирование магического метода __add__, возвращающего сумму произведений цены на количество у двух товаров"""
    assert product_casio + add_product1 == 2398.00
