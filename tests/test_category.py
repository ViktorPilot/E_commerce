import pytest

from src.category import Category
from src.prod_grass import LawnGrass
from src.prod_smartphone import Smartphone
from src.product import Product


def test_init_category_valid(
    category_electronics: Category, category_sports: Category, category_relax: Category
) -> None:
    """Тестирование создания экземпляров класса 'Category', работы счетчика категорий и счетчика товаров
    при валидных значениях"""
    assert category_electronics.name == "watch"
    assert category_electronics.description == "for_time"
    assert category_electronics.product_count == 4

    assert category_electronics.category_count == 3
    assert category_sports.category_count == 3

    assert category_electronics.product_count == 4
    assert category_sports.product_count == 4


def test_add_product_one_class_1(category_electronics: Category, add_product1: Product) -> None:
    """Тестирование метода класса, позволяющего добавлять товар в категорию, если товары из одного класса"""
    category_electronics.add_product(add_product1)
    assert category_electronics.product_count == 4
    assert add_product1.name == "g-shock"


def test_add_product_one_class_2(category_electronics: Category, grass_1: LawnGrass, smartphone_1: Smartphone) -> None:
    """Тестирование метода класса, позволяющего добавлять товар в категорию,
    если добавляемый товар из дочернего класса"""
    category_electronics.add_product(grass_1)
    category_electronics.add_product(smartphone_1)
    assert category_electronics.product_count == 5
    assert grass_1.name == "Газонная трава"
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"


def test_add_product_no_one_class(category_electronics: Category) -> None:
    """Тестирование метода класса, позволяющего добавлять товар в категорию,
    если добавляемый товар не принадлежит этому и дочерним классам"""
    with pytest.raises(TypeError):
        category_electronics.add_product("unexpect_product")  # type: ignore


def test_products(category_electronics: Category, add_product1: Product) -> None:
    """Тестирование геттера, возвращающего строку информации о товарах заданной категории"""
    category_electronics.add_product(add_product1)
    assert category_electronics.products == (
        "casio, 100.0 руб. Остаток: 4 шт.\n"
        "iwatch, 150.0 руб. Остаток: 2 шт.\n"
        "brightling, 300.0 руб. Остаток: 5 шт.\n"
        "g-shock, 333.0 руб. Остаток: 6 шт.\n"
    )


def test_str_category(category_electronics: Category) -> None:
    """Тестирование магического метода __str__, возвращающего строку с названием категории
    и общем количестве товаров в ней"""
    assert str(category_electronics) == "watch, количество продуктов: 11 шт."
