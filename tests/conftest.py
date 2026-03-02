import pytest

from src.category import Category
from src.iterator_prod import IteratorProduct
from src.order import OrderProduct
from src.prod_grass import LawnGrass
from src.prod_smartphone import Smartphone
from src.product import Product


@pytest.fixture
def product_casio() -> Product:
    return Product("casio", "for_current_time", 100.00, 4)


@pytest.fixture
def category_electronics() -> Category:
    return Category(
        "watch",
        "for_time",
        [
            Product("casio", "for_current_time", 100.00, 4),
            Product("iwatch", "for_current_time", 150.00, 2),
            Product("brightling", "for_current_time", 300.00, 5),
        ],
    )


@pytest.fixture
def category_sports() -> Category:
    return Category("sports", "for_game", [Product("ball", "for_game", 20.00, 8)])


@pytest.fixture
def category_relax() -> Category:
    return Category("relax", "for_pleasure", [])


@pytest.fixture
def get_categories_and_products_valid() -> list[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных"
            " функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    Product.list_product = []
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def add_product1() -> Product:
    return Product("g-shock", "for_current_time", 333.00, 6)


@pytest.fixture
def iterator_1(category_electronics: Category) -> IteratorProduct:
    return IteratorProduct(category_electronics)


@pytest.fixture
def smartphone_1() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass_1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def order_1() -> OrderProduct:
    return OrderProduct("Ford", 1, 300.55)
