from src.category import Category
from src.product import Product

class IteratorProduct:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.start_idx = -1
        return self

    def __next__(self):
        self.list_prod = self.category.products.strip().split("\n")
        if self.start_idx < len(self.list_prod) - 1:
            self.start_idx += 1
            return self.list_prod[self.start_idx]
        else:
            raise StopIteration


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iter_1 = IteratorProduct(category1)
    for _ in iter_1:
       print(_)
