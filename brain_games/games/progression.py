#!/usr/bin/env python
from random import randint


TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    """
    формирует арифметическую прогрессию произвольной длины (от 5 до 10)
    с произвольно пропущенным элементом (но не крайним)

    Returns
    -------
    возвращает пропущенный элемент арифметической прогрессии\n
    question - строка-вопрос текущего раунда
    """
    min_number = 1
    max_number = 10
    first = randint(min_number, max_number)
    length = randint(max_number / 2, max_number)
    step = randint(min_number, max_number)
    skip = randint(min_number + 1, (length - 2))
    sequence_list = [str(first)]
    for i in range(1, length):
        first += step
        if i == skip:
            sequence_list.append('..')
            correct_answer = first
        else:
            sequence_list.append(str(first))
    question = " ".join(sequence_list)
    return str(correct_answer), question
