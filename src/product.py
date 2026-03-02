from __future__ import annotations

from typing import Any

from src.base import BaseProduct
from src.mixin_prod import ProductMixin


class Product(BaseProduct, ProductMixin):
    """Класс товары из категорий"""

    name: str
    description: str
    price: float
    quantity: int
    list_product: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса 'Product'"""
        self.__price = price
        super().__init__(name, description, quantity)
        Product.list_product.append((name, price, quantity))
        ProductMixin.__init__(self)
    def __str__(self) -> str:
        """Реализация магического метода __str__, возвращающего информацию о товаре"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Реализация магического метода __add__, возвращающего сумму произведений цены на количество
        у двух товаров из одной категории"""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("Товары не находятся в одной категории. Сложение невозможно.")

    @classmethod
    def new_product(cls, product: dict) -> Product:
        """Классметод преобразования словаря с параметрами товара в объект 'Product'.
        Суммирует количество товара, имеющее одинаковое наименование и сохраняет максимальную цену товара"""
        for i in cls.list_product:
            if product["name"] == i[0]:
                product["price"] = max(i[1], product["price"])
                product["quantity"] += i[2]
                cls.list_product.remove(i)
        return cls(**product)

    @property
    def price(self) -> float:
        """Геттер, позволяющий вызывать цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер, позволяющий изменять цену товара.
        Если новая цена менее старой пользователь имеет возможность оставить предидущую цену или заменить на новую.
        При отрицательных значениях цены дополнительно выводит информацию об этом в консоль."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            while True:
                answer = input("Введите y/n для подтверждения снижения цены:\n").strip().lower()
                if answer == "n":
                    break
                elif answer != "y":
                    print("Введен неверный ответ.")
                    continue
                else:
                    self.__price = new_price
                    break
        else:
            self.__price = new_price


if __name__ == "__main__":  # pragma:no cover
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

print(Product.__mro__)