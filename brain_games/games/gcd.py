#!/usr/bin/env python
from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """
    функция находит наибольший общий делитель для двух чисел

    Returns
    -------
    возвращает НОД\n
    question - строка-вопрос текущего раунда
    """
    min_number = 1
    max_number = 100
    a = randint(min_number, max_number)
    b = randint(min_number, max_number)
    question = f"{a} {b}"
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        return str(a), question
