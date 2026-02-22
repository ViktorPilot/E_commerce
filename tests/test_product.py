from unittest.mock import patch

from src.product import Product


def test_init_product_valid(product_casio: Product) -> None:
    """Тестирование создания экземпляра класса 'Product' при валидных значениях"""
    assert product_casio.name == "casio"
    assert product_casio.description == "for_current_time"
    assert product_casio.price == 100.00
    assert product_casio.quantity == 4


def test_new_product(product_casio: Product) -> None:
    """Тестирование классметода, позволяющего создать объект класса 'Product',
    суммирущего общее количество и выбирающего максимальную цену товара при одинаковом его названии"""
    product2 = Product.new_product({"name": "casio", "description": "for_current_time", "price": 80.00, "quantity": 8})
    assert product2.name == "casio"
    assert product2.price == 100.00
    assert product2.quantity == 12


def test_price_getter(product_casio: Product) -> None:
    """Тестирование геттера класса 'Product', позволяющего вызвать цену приватного товара"""
    assert product_casio.price == 100.00


@patch("builtins.input")
def test_price_setter(mock_input, capsys, product_casio: Product) -> None:
    """Тестирование сеттера класса 'Product', позволяющего изменять цену товара"""

    # при новой цене больше 0 и больше старого значения
    product_casio.price = 200.00
    assert product_casio.price == 200.00

    # при новой цене меньше 0 и меньше старого значения
    # при выборе пользователя - оставить старое значение цены
    mock_input.return_value = "n"
    product_casio.price = - 100.00
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product_casio.price == 200.00

    # при новой цене больше 0, но меньше старого значения
    # при выборе пользователя - изменить старое значение цены на новое
    mock_input.return_value = "y"
    product_casio.price = 50.00
    assert product_casio.price == 50.00

    # при вводе неверного ответа при первой попытке
    product_casio.price = 50.00
    mock_input.side_effect = ["a", "y"]
    assert product_casio.price == 50.00
