class QuantityException(Exception):
    """Создание класса-исключения при инициализации товара с нулевым количеством"""

    def __init__(self, *args: str) -> None:
        """Инициализация сообщения об исключении"""
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self) -> str:
        """Реализация текста сообщения при возникновении исключения"""
        return self.message
