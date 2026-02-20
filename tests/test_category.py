from src.category import Category


def test_init_category_valid(
    category_electronics: Category, category_sports: Category, category_relax: Category
) -> None:
    """Тестирование создания экземпляров класса 'Category', работы счетчика категорий и счетчика товаров
    при валидных значениях"""
    assert category_electronics.name == "watch"
    assert category_electronics.description == "for_time"
    assert len(category_electronics.products) == 3

    assert category_electronics.category_count == 3
    assert category_sports.category_count == 3

    assert category_electronics.product_count == 4
    assert category_sports.product_count == 4
