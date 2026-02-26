import pytest

from src.iterator_prod import IteratorProduct


def test_iterator_start_idx(iterator_1: IteratorProduct) -> None:
    """Тестирование работы итератора товаров заданной категории"""
    # проверка начального значения индекса итератора
    assert iterator_1.start_idx == -1

    # тестирование работы итератора последовательным вызовом товаров
    assert next(iterator_1) == "casio, 100.0 руб. Остаток: 4 шт."
    assert next(iterator_1) == "iwatch, 150.0 руб. Остаток: 2 шт."
    assert next(iterator_1) == "brightling, 300.0 руб. Остаток: 5 шт."

    # тестирование формирования исключения после окончания перебора всех товаров
    with pytest.raises(StopIteration):
        next(iterator_1)
