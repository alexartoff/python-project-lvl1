#!/usr/bin/env python
from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """
    функция проверяет на четность рандомное число

    Returns
    -------
    возвращает "yes" если четное\n
    question - строка-вопрос текущего раунда
    """
    min_number = 1
    max_number = 100
    question = randint(min_number, max_number)
    if question % 2 == 0:
        return 'yes', str(question)
    return 'no', str(question)
