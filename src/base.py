from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Создание базового класса для класса товаров"""

    @abstractmethod
    def __init__(self, name: str, description: str, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.quantity = quantity
        super().__init__()

    @abstractmethod
    def __add__(self, other: Any) -> None:
        pass
