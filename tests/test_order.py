from typing import Any

from src.order import OrderProduct


def test_order_init(capsys: Any, order_1: OrderProduct) -> None:
    """Тестирование инициализации товара категории 'OrderProduct' при валидных значениях"""
    assert order_1.name == "Ford"
    assert order_1.quantity == 1
    capture = capsys.readouterr()
    assert capture.out.strip().split("\n")[0] == "Товар успешно добавлен"
    assert capture.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


def test_order_str(order_1: OrderProduct) -> None:
    """Тестирование магического метода __str__, возвращающего строку с названием,
    количеством и стоимостью товара"""
    assert str(order_1) == "Ford, количество: 1, стоимость: 300.55"


def test_order_init_exception(capsys: Any, order_2: OrderProduct) -> None:
    """Тестирование обработки исключения при добавлении товара с нулевым количеством"""
    capture = capsys.readouterr()
    assert capture.out.strip().split("\n")[0] == "Товар с нулевым количеством не может быть добавлен"
    assert capture.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


def test_order_str_exception(order_2: OrderProduct) -> None:
    """Тестирование обработки исключения при попытке получения доступа к атрибутам несуществующего товара"""
    assert str(order_2) == "Попытка доступа к атрибутам несуществующего товара"
