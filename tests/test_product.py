from src.product import Product


def test_init_product_valid(product_casio: Product) -> None:
    """Тестирование создания экземпляра класса 'Product' при валидных значениях"""
    assert product_casio.name == "casio"
    assert product_casio.description == "for_current_time"
    assert product_casio.price == 100.00
    assert product_casio.quantity == 4
