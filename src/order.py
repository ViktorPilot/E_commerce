from src.base_cat_and_ord import BaseCatOrd
from src.exception_cat_and_ord import QuantityException


class OrderProduct(BaseCatOrd):
    """Создание класса купленных товаров"""

    def __init__(self, name: str, quantity: int, price: float) -> None:
        """Инициализация экземпляра класса купленного товара"""
        try:
            if quantity == 0:
                raise QuantityException("Товар с нулевым количеством не может быть добавлен")
        except QuantityException as e:
            print(str(e))
        else:
            self.quantity = quantity
            self.name = name
            self.__price = price
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self) -> str:
        """Реализация магического метода __str__, возвращающего строку с названием,
        общем количестве и стоимости купленного товара"""
        try:
            return f"{self.name}, количество: {self.quantity}, стоимость: {self.__price}"
        except AttributeError:
            return "Попытка доступа к атрибутам несуществующего товара"


if __name__ == "__main__":  # pragma: no cover
    car1 = OrderProduct("Ford", 0, 1111)
    car2 = OrderProduct("Ford", 3, 1222)
    print(str(car1))
    print(str(car2))
