#!/usr/bin/env python
from math import sqrt
from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_data_from_game():
    """
    функция проверяет словарь prime_dict, сформированный функцией
    make_dict_for_check на наличие (value.count) ложных значений в словаре

    Returns
    -------
    возвращает "yes" если число является простым (False нет в prime_dict)\n
    question - строка-задание текущего раунда
    """
    min_number = 1
    max_number = 100
    question = randint(min_number, max_number)
    prime_dict = make_dict_for_check(question)
    for value in prime_dict.values():
        if value.count(False) == 0:
            return "yes", str(question)
        return "no", str(question)


def make_dict_for_check(num):
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
    out_dict = {num: []}
    for i in range(2, (round(sqrt(num)) + 1)):
        if num > i:
            if num % i >= 1:
                out_dict[num].append(True)
            elif num % i == 0:
                out_dict[num].append(False)
    return out_dict
