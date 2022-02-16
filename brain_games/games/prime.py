#!/usr/bin/env python
from math import sqrt
from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    """
    функция передаёт число на проверку в функцию is_pime()

    Returns
    -------
    возвращает "yes" если число является простым\n
    question - строка-вопрос текущего раунда
    """
    min_number = 1
    max_number = 100
    question = randint(min_number, max_number)
    if is_prime(question):
        return 'yes', str(question)
    return 'no', str(question)


def is_prime(num):
    """
    функция проверяет является ли простым полученное число

    Parameter
    ---------
    num - число int

    Returns
    -------
    возвращает False если встречается остаток от деления = 0\n
    если этого не произошло, вернётся True
    """
    if num < 2:
        return False
    else:
        for i in range(2, (round(sqrt(num)) + 1)):
            if num > i:
                if num % i == 0:
                    return False
        return True
