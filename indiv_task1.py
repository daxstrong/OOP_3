#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Any


def _is_number(value) -> bool:
    """
    Проверяет, можно ли преобразовать значение в число с плавающей запятой.
    :param value: Значение для проверки
    :return: True, если значение является числом, иначе False
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Point:
    def __init__(self, first: float = 0.0, second: float = 0.0):
        """
        Инициализирует точку с двумя координатами (first и second).
        :param first: Координата X точки
        :param second: Координата Y точки
        """
        if not _is_number(first) or not _is_number(second):
            raise ValueError("Координаты должны быть числами!")

        self.first = float(first)
        self.second = float(second)

    def read(self):
        """
        Ввод координат точки с клавиатуры.
        """
        first_input = input('Введите координату X: ')
        if not _is_number(first_input):
            raise ValueError('Координата должна быть числом!')

        second_input = input('Введите координату Y: ')
        if not _is_number(second_input):
            raise ValueError('Координата должна быть числом!')

        self.first = float(first_input)
        self.second = float(second_input)

    def display(self):
        """
        Вывод координат точки на экран.
        """
        print(f'Точка: ({self.first}, {self.second})')

    def distance(self) -> float:
        """
        Вычисляет расстояние от точки до начала координат.
        :return: Расстояние от начала координат до точки
        """
        return math.sqrt(self.first ** 2 + self.second ** 2)

    def __add__(self, other: Any) -> 'Point':
        if isinstance(other, Point):
            return Point(self.first + other.first, self.second + other.second)
        return NotImplemented

    def __sub__(self, other: Any) -> 'Point':
        if isinstance(other, Point):
            return Point(self.first - other.first, self.second - other.second)
        return NotImplemented

    def __mul__(self, scalar: float) -> 'Point':
        if _is_number(scalar):
            return Point(self.first * scalar, self.second * scalar)
        return NotImplemented

    def __rmul__(self, scalar: float) -> 'Point':
        return self.__mul__(scalar)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Point):
            return self.first == other.first and self.second == other.second
        return NotImplemented

    def __ne__(self, other: Any) -> bool:
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    def __str__(self) -> str:
        return f'Точка({self.first}, {self.second})'

    def __repr__(self) -> str:
        return f'Point(first={self.first}, second={self.second})'


def make_point(first: float, second: float) -> Point:
    """
    Создает объект Point с заданными координатами.
    :param first: Координата X
    :param second: Координата Y
    :return: Объект Point
    :raises ValueError: Если аргументы не являются числами
    """
    if not _is_number(first) or not _is_number(second):
        raise ValueError("Координаты должны быть числами!")
    return Point(first, second)


if __name__ == '__main__':
    # Пример использования класса Point с перегруженными операторами
    try:
        # Создание точек с помощью функции make_point
        point1 = make_point(3.0, 4.0)
        point2 = make_point(1.0, 2.0)
        print("Исходные точки:")
        point1.display()
        point2.display()

        # Сложение точек
        point3 = point1 + point2
        print("\nСумма точек:")
        point3.display()

        # Вычитание точек
        point4 = point1 - point2
        print("\nРазность точек:")
        point4.display()

        # Умножение точки на скаляр
        scalar = 2
        point5 = point1 * scalar
        print(f"\nУмножение точки {point1} на скаляр {scalar}:")
        point5.display()

        # Проверка равенства точек
        print("\nПроверка равенства точек:")
        print(f"point1 == point2: {point1 == point2}")
        print(f"point1 == make_point(3.0, 4.0): {point1 == make_point(3.0, 4.0)}")

        # Ввод координат с клавиатуры для point2
        print("\nВвод новых координат для point2:")
        point2.read()
        point2.display()

        # Вычисление расстояния до начала координат
        distance = point2.distance()
        print(f'Расстояние точки {point2} до начала координат: {distance:.2f}')

    except ValueError as e:
        print("Ошибка:", e)