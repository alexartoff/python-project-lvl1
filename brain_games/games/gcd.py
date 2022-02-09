#!/usr/bin/env python
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def game_mechanics():
    """
    функция находит наибольший общий делитель для двух чисел

    Returns
    -------
    возвращает НОД\n
    question - строка-задание текущего раунда
    """
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        return str(a), question
