#!/usr/bin/env python
from random import randint


def find_gcd():
    """
    функция находит наибольший общий делитель для двух чисел

    Returns
    -------
    возвращает НОД
    """
    a = randint(1, 100)
    b = randint(1, 100)
    task = ("{} {}".format(a, b))
    print("Question:", task)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        return str(a)
