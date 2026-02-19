import os.path
from unittest.mock import Mock, patch

import pytest

from src.read_products_json import get_categories_and_products

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


@patch("src.read_products_json.json")
def test_get_categories_and_products_valid(mock_json: Mock, get_categories_and_products_valid: list[dict]) -> None:
    """Тестирование создания объектов класса 'Category' и 'Product' из файла при валидных значениях"""
    mock_json.load.return_value = get_categories_and_products_valid
    result = get_categories_and_products(os.path.join(BASE_DIR, "data/products.json"))
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
    assert result[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert result[1].products[0].price == 123000.0


@patch("src.read_products_json.json")
def test_get_categories_and_products_not_path(mock_json: Mock, get_categories_and_products_valid: list[dict]) -> None:
    """Тестирование работы функции при несуществующем пути до файла"""
    mock_json.load.return_value = get_categories_and_products_valid
    with pytest.raises(ModuleNotFoundError):
        get_categories_and_products("../direct/products.json")
