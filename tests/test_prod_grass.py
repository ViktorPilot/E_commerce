from src.prod_grass import LawnGrass


def test_init_grass(grass_1: LawnGrass) -> None:
    """Тестирование инициализации товара категории 'LawnGrass' при валидных значениях"""
    assert grass_1.name == "Газонная трава"
    assert grass_1.price == 500.0
    assert grass_1.country == "Россия"
    assert grass_1.color == "Зеленый"
