from typing import Any

from src.prod_grass import LawnGrass
from src.prod_smartphone import Smartphone
from src.product import Product


def test_product_mixin_1(capsys: Any, product_casio: Product) -> None:
    """Тестирование вывода миксином информации о товаре класса 'Product' в консоль"""
    capture = capsys.readouterr()
    assert capture.out.strip() == "Product(casio, for_current_time, 100.0, 4)"


def test_smartphone_mixin_2(capsys: Any, smartphone_1: Smartphone) -> None:
    """Тестирование вывода миксином информации о товаре класса 'Smartphone' в консоль"""
    capture = capsys.readouterr()
    assert capture.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_grass_mixin_3(capsys: Any, grass_1: LawnGrass) -> None:
    """Тестирование вывода миксином информации о товаре класса 'LawnGrass' в консоль"""
    capture = capsys.readouterr()
    assert capture.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
