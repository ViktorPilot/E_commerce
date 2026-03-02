from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Создание базового класса для класса товаров"""
    @abstractmethod
    def __init__(self, name: str, description: str, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        super().__init__()
        pass

    @abstractmethod
    def __add__(self, other: Any) -> None:
        pass