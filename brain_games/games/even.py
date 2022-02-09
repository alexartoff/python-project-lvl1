#!/usr/bin/env python
from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_mechanics():
    """
    функция проверяет на четность рандомное число

    Returns
    -------
    возвращает "yes" если четное\n
    num - строка-задание текущего раунда
    """
    num = randint(1, 100)
    if num % 2 == 0:
        return "yes", str(num)
    return "no", str(num)
