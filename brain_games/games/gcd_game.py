#!/usr/bin/env python


def find_gcd(a, b):
    """
    функция находит наибольший общий делитель для двух чисел

    Returns
    -------
    возвращает НОД
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        return a
