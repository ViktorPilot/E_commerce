class Category:
    """Класс категории товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициализация экземпляра класса 'Category'"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)


if __name__ == "__main__":
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )
