import doctest


class Buildings:
    """Базовый класс зданий"""

    def __init__(self, kind: str, floors: int, entrances: int, elevator: bool):
        self.kind = kind
        self.floors = floors
        self.entrances = entrances
        self.elevator = elevator

    def __str__(self) -> str:
        return f'{self.kind} с {self.floors} этажами'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(kind={self.kind!r}, floors={self.floors!r}, " \
               f"entrances={self.entrances!r}, elevator={self.elevator!r})"

    def elevator_repair(self) -> None:
        """
        План действий при поломке лифта.

        Пример:
        >>> building = Buildings('Жилой дом', 8, 5, True)
        >>> building.elevator_repair()
        """
        ...

    def entrances_info(self, open_entrances: int) -> str:
        """
        Информация по открытым входам.
        :param open_entrances: Количество открытых входов

        Пример:
        >>> building = Buildings('Жилой дом', 8, 5, True)
        >>> building.entrances_info(5)
        'Все входы работают'
        """
        if open_entrances == self.entrances:
            return 'Все входы работают'
        else:
            return 'Некоторые входы заблокированы'


class University(Buildings):
    """Дочерний класс Университет"""

    def __init__(self, kind: str, floors: int, entrances: int, elevator: bool, cafeterias: int):
        super().__init__(kind, floors, entrances, elevator)
        self.cafeterias = cafeterias

    def __repr__(self):
        return f"{self.__class__.__name__}(kind={self.kind!r}, floors={self.floors!r}, " \
               f"entrances={self.entrances!r}, elevator={self.elevator!r}, cafeterias={self.cafeterias!r})"

    def elevator_repair(self) -> None:
        """
        План действий при поломке лифта.

        Пример:
        >>> building = Buildings('Жилой дом', 8, 5, True)
        >>> building.elevator_repair()
        """
        super().elevator_repair()
        ...

    def entrances_info(self, open_entrances: int) -> str:
        """
        Информация по открытым входам.
        Перегрузка метода необходима из-за измененя входных данных с добавлением
        атрибуда в дочернем классе.
        :param open_entrances: Количество открытых входов.

        Пример:
        >>> building = University('СПбГУ', 3, 5, False, 2)
        >>> building.entrances_info(5)
        'Все входы работают, а также открыты 2 входа из кафетериев'
        """

        if open_entrances == self.entrances:
            return f'Все входы работают, а также открыты {self.cafeterias} входа из кафетериев'
        else:
            return f'Некоторые входы заблокированы, {self.cafeterias} входа из кафетериев открыты'


if __name__ == "__main__":
    doctest.testmod()
    pass
