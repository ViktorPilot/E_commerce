from abc import ABC, abstractmethod


class BaseCatOrd(ABC):
    """Создание базового класса для класса 'Category' и 'Order'"""

    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
