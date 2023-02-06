class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    
    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages) -> None:
        if not isinstance(pages, int):
            raise TypeError(f"Количество страниц должно быть типа int, не {type(pages)}")
        if not pages > 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()
    
    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, duration) -> None:
        if not isinstance(duration, float):
            raise TypeError(f"Длительность книги должна быть типа float, не {type(duration)}")
        if not duration > 0:
            raise ValueError("Длительность книги должна быть положительной")
        self.duration = duration
