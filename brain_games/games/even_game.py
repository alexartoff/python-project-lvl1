#!/usr/bin/env python


def is_even(num):
    """
    функция проверяет на четность число

    Parameters
    ----------
    num - число для проверки

    Returns
    -------
    возвращает True если четное
    """
    if num % 2 == 0:
        return True
    else:
        return False
