from typing import Union
import doctest


class Door:
    def __init__(self, material: str, width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Дверь".

        :param material: Материал двери
        :param width: Ширина двери в сантиметрах
        :param height: Высота двери в сантиметрах

        Примеры:
        >>> door = Door("Wood", 80, 210)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material
        if not isinstance(width, (int, float)):
            raise TypeError("Ширинна должен быть типа int или float")
        if not width > 0:
            raise ValueError("Ширина не может быть меньше нуля")
        self.width = width
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должен быть типа int или float")
        if not height > 0:
            raise ValueError("Высота не может быть меньше нуля")
        if width > height:
            raise ValueError("Высота двери должна быть больше её ширины")
        self.height = height

    def open_the_door(self, key: bool, type_of_key: bool):
        """
        Функция, которая открывает дверь.

        :param key: Наличие у пользователя ключа
        :param type_of_key: Подходящий ли это ключ

        Примеры:
        >>> door = Door("Wood", 80, 210)
        >>> door.open_the_door(True, False)
        """
        if key is not True:
            raise ValueError("У вас нет ключа")
        if type_of_key is not True:
            raise ValueError("Ваш ключ не подходит")
        ...

    def look_at_peephole(self):
        """
        Функция, которая выполняет действие 'Посмотреть в глазок двери'.

        Примеры:
        >>> door = Door("Wood", 80, 210)
        >>> door.look_at_peephole()
        """
        ...


class Meat:
    def __init__(self, type_of_meat: str, weight: Union[int, float], freshness: bool):
        """
        Создание и подготовка к работе объекта "Мясо".

        :param type_of_meat: Сорт мяса
        :param weight: Вес мяса в граммах
        :param freshness: Свежесть мяса

        Примеры:
        >>> meat = Meat("Chiken breast", 200, True)
        """
        if not isinstance(type_of_meat, str):
            raise TypeError("Сорт мяса должен быть типа str")
        self.type_of_meat = type_of_meat
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if not weight > 0:
            raise ValueError("Вес должен быть типа int или float")
        self.weight = weight
        if not isinstance(freshness, bool):
            raise TypeError("Свежесть должна быть типа bool")
        if freshness is not True:
            raise ValueError("Мясо должно быть свежим")
        self.freshness = freshness

    def buy_meat(self, shopping_list: dict, weight: Union[int, float], money: Union[int, float]):
        """
        Функция, которая выполняет покупку мяса.

        :param shopping_list: Список необходимых покупок
        :param weight: Вес мяса, который нам взвесил продавец
        :param money: Наш бюджет на покупки в рублях
        :return: Количество оставшихся денег

        Примеры:
        >>> meat = Meat("Chiken breast", 200, True)
        >>> meat.buy_meat({"weight": 200}, 200, 1312)
        """
        if weight == shopping_list["weight"] is False:
            raise ValueError("Вам нужно купить мяса, сколько указано в списке покупок")
        ...

    def cut_meat(self, knife: bool, sharpness: bool):
        """
        Функция, которая выпоняет резку мяса.

        :param knife: Наличие чистого ножа
        :param sharpness: Острый ли наш нож

        Примеры:
        >>> meat = Meat("Chiken breast", 200, True)
        >>> meat.cut_meat(True, False)
        """
        if sharpness is not True:
            raise ValueError("Тупой нож")
        ...

    def time_of_cooking(self, frying_pan: bool, oil: bool, recipe: dict):
        """
        Функция, которая показывает затрату времени на готовку.

        :param frying_pan: Наличие чситой сковороды
        :param oil: Наличие масла
        :param recipe: Рецепт приготовления блюда
        :return: Время, затраченное на готовку

        Примеры:
        >>> meat = Meat("Chiken breast", 200, True)
        >>> meat.time_of_cooking(True, False, {})
        """
        if frying_pan is not True:
            raise ValueError("У вас нет сковороды")
        if frying_pan is not True:
            raise ValueError("Вам необходимо масло")
        ...


class Cards:
    def __init__(self, amount: int, size: Union[int, float], deck: int):
        """
        Создание и подготовка к работе объекта "Карты".

        :param amount: Количество карт
        :param size: Размеры карт в квадратных сантиметрах
        :param deck: Какая играет колода

        Примеры:
        >>> cards = Cards(33, 20, 32)
        """
        if not isinstance(amount, int):
            raise TypeError("Количество карт должно быть типа int")
        if not amount > 0:
            raise ValueError("Количество карт не может быть меньше нуля")
        self.amount = amount
        if not isinstance(size, (int, float)):
            raise TypeError("Размер карт должен быть типа int или float")
        if not size > 0:
            raise ValueError("Размер карт не может быть меньше нуля")
        self.size = size
        if not isinstance(deck, int):
            raise TypeError("Колода должна быть типа int")
        if amount < deck:
            raise ValueError("Неиграбельно, должна быть целая колода карт")
        self.deck = deck

    def playing(self, name_of_game: str, amount_of_players: int, all_players_knew_rules: bool):
        """
        Функция описания игры в карты.

        :param name_of_game: Название игры
        :param amount_of_players: Количество игроков
        :param all_players_knew_rules: Знакомы ли все игроки с правилами игры
        :return: Словарь {Имя игрока: количество побед}

        Примеры:
        >>> cards = Cards(33, 20, 32)
        >>> cards.playing("Тысяча", 5, False)
        """
        if not amount_of_players > 0:
            raise ValueError("Где игроки?")
        if amount_of_players > 4:
            print("Слишком много игроков")
        if all_players_knew_rules is not True:
            raise ValueError("Сперва объясните всем игрокам правила")
        ...

    def distribute(self, players_list: list, amount_of_players: int, deception: bool):
        """
        Раздача карт игрокам.

        :param players_list: Список имен зарегестрированных игроков
        :param amount_of_players: Количество пришедших игроков
        :param deception: Попытка жульничества при раздаче

        Примеры:
        >>> cards = Cards(33, 20, 32)
        >>> cards.distribute(["Коля", "Вася", "Маша"], 5, True)
        """
        if deception is not True:
            raise ValueError('Вас выгнали за попытку жульничества при раздаче карт')


if __name__ == "__main__":
    doctest.testmod()
    pass
