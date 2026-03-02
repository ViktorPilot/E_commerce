from typing import Any

from src.base_cat_and_ord import BaseCatOrd
from src.product import Product


class Category(BaseCatOrd):
    """Класс категории товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициализация экземпляра класса 'Category'"""
        super().__init__(name)
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)
        self.quantity = 0

    def __str__(self) -> str:
        """Реализация магического метода __str__, возвращающего строку с названием категории
        и общем количестве товаров в ней"""
        for product in self.__products:
            self.quantity += product.quantity
        return f"{self.name}, количество продуктов: {self.quantity} шт."

    def add_product(self, product: Any) -> None:
        """Метод класса, позволяющий добавлять товар к списку товаров заданной категории,
        если он является экземпляром этого или дочерних классов"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Товар не принадлежит разрешенным для добавления категориям.")

    @property
    def products(self) -> str:
        """Геттер, возвращающий строку с информацией о товарах заданной категории"""
        products_str = ""
        for product in self.__products:
            products_str += str(product) + "\n"
        return products_str


if __name__ == "__main__":  # pragma:no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)
