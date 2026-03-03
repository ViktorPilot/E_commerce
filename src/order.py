from src.base_cat_and_ord import BaseCatOrd


class OrderProduct(BaseCatOrd):
    """Создание класса купленных товаров"""

    def __init__(self, name: str, quantity: int, price: float) -> None:
        """Инициализация экземпляра класса купленного товара"""
        super().__init__(name)
        self.name = name
        self.quantity = quantity
        self.__price = price

    def __str__(self) -> str:
        """Реализация магического метода __str__, возвращающего строку с названием,
        общем количестве и стоимости купленного товара"""
        return f"{self.name}, количество: {self.quantity}, стоимость: {self.__price}"


if __name__ == "__main__":  # pragma: no cover
    car1 = OrderProduct("Ford", 1, 300.50)
    print(car1)
