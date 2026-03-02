from src.order import OrderProduct


def test_order_init(order_1: OrderProduct) -> None:
    """Тестирование инициализации товара категории 'OrderProduct' при валидных значениях"""
    assert order_1.name == "Ford"
    assert order_1.quantity == 1

def test_order_str(order_1: OrderProduct) -> None:
    """Тестирование магического метода __str__, возвращающего строку с названием,
       количеством и стоимости товара"""
    assert str(order_1) == "Ford, количество: 1, стоимость: 300.55"
