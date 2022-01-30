#!/usr/bin/env python
from random import randint


def is_even():
    """
    функция проверяет на четность рандомное число

    Returns
    -------
    возвращает "yes" если четное
    """
    num = randint(1, 100)
    print("Question:", num)
    if num % 2 == 0:
        return "yes"
    else:
        return "no"
