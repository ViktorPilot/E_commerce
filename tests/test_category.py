from src.category import Category
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


def test_add_product(category_electronics: Category, add_product1: Product) -> None:
    """Тестирование метода класса, вызывающего товар с приватным уровнем доступа"""
    category_electronics.add_product(add_product1)
    assert category_electronics.product_count == 4
    assert add_product1.name == "g-shock"


def test_products(category_electronics: Category, add_product1: Product) -> None:
    """Тестирование геттера, возвращающего строку информации о товарах заданной категории"""
    category_electronics.add_product(add_product1)
    assert category_electronics.products == (
        "casio, 100.0 руб. Остаток: 4 шт.\n"
        "iwatch, 150.0 руб. Остаток: 2 шт.\n"
        "brightling, 300.0 руб. Остаток: 5 шт.\n"
        "g-shock, 333.0 руб. Остаток: 6 шт.\n"
    )
