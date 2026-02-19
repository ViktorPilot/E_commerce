import json
import os.path

from src.category import Category
from src.product import Product


def get_categories_and_products(path_to_products: str) -> list:
    """Получение списка объектов класса 'Category', содержащего в себе списки объектов класса 'Product'"""
    if os.path.exists(path_to_products):
        with open(path_to_products, "r", encoding="utf-8") as f:
            result = json.load(f)
    else:
        raise ModuleNotFoundError(f"Файл по адресу {path_to_products} не найден. Проверьте путь до файла.")
    list_category = []

    for categories in result:
        list_product = []
        for prod in categories["products"]:
            list_product.append(Product(**prod))
        categories["products"] = list_product
        list_category.append(Category(**categories))
    return list_category


if __name__ == "__main__":
    res = get_categories_and_products("../data/products.json")
    print(res[0].name)
