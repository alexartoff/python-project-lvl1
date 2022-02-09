#!/usr/bin/env python
from math import sqrt
from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_mechanics():
    """
    функция проверяет словарь prime_dict, сформированный функцией
    check_num на наличие (value.count) ложных значений в словаре

    Returns
    -------
    возвращает "yes" если число является простым\n
    num - строка-задание текущего раунда
    """
    num = randint(1, 100)
    prime_dict = check_num(num)
    for value in prime_dict.values():
        if value.count(False) > 0:
            return "no", str(num)
        elif value.count(False) == 0:
            return "yes", str(num)


def check_num(num):
    """
    функция формирует словарь со списком результатов вычисления по
    критериям простых чисел в диапазоне от 2 до округл. sqrt(num)

    Parameters
    ----------
    num - число для проверки

    Returns
    -------
    возвращает словарь ключ-число num, значение-список результатов
    вычисления по критериям простых чисел в булевом типе
    """
    out = {num: [True, ]}
    for i in range(2, (round(sqrt(num)) + 1)):
        if num % i >= 1 and num > i:
            out[num].append(True)
        elif num % i == 0 and num > i:
            out[num].append(False)
    return out