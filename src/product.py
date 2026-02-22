class Product:
    """Класс товары из категорий"""

    name: str
    description: str
    price: float
    quantity: int
    list_product = []
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса 'Product'"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.list_product.append((name, price, quantity))

    @classmethod
    def new_product(cls, product: dict):
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
        if new_price < self.__price:
            while True:
                answer = input("Введите y/n для подтверждения снижения цены:\n").strip().lower()
                if answer == "n":
                    self.__price = self.__price
                    break
                elif answer != "y":
                    print("Введен неверный ответ.")
                    continue
                else:
                    self.__price = new_price
                    break
        else:
            self.__price = new_price


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product.new_product({"name": "casio", "description": "for_current_time", "price": 100.00, "quantity": 7})
    product3 = Product.new_product({"name": "casio", "description": "for_current_time", "price": 80.00, "quantity": 8})
    print(product3.quantity)