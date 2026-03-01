from src.prod_smartphone import Smartphone


def test_init_grass(smartphone_1: Smartphone) -> None:
    """Тестирование инициализации товара категории 'Smartphone' при валидных значениях"""
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"
