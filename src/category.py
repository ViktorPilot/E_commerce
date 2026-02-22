from src.product import Product


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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Метод класса, позволяющий вызывать приватный атрибут списка продуктов"""
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        """Геттер, возвращающий строку с информацией о товарах."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str


if __name__ == "__main__":
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    product4 = Product("S G S23 Ultra", "Серый", 180000.0, 5)
    category1.add_product(product4)
    product5 = Product("Ultra", "Серый", 180000.0, 5)
    category1.add_product(product5)
    print(category1.products)