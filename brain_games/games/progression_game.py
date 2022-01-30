#!/usr/bin/env python
from random import randint


def progression():
    """
    формирует арифметическую прогрессию произвольной длины (от 5 до 10)
    с произвольно пропущенным элементом (но не крайним)

    Returns
    -------
    возвращает пропущенный элемент арифметической прогрессии
    """
    first = randint(1, 10)
    count = randint(5, 10)
    step = randint(1, 10)
    skip = randint(2, (count - 2))
    task_line = "{} ".format(str(first))
    next_element = first
    for i in range(1, count):
        next_element += step
        if i == skip:
            task_line += ".. "
            correct_answer = next_element
        else:
            task_line += "{} ".format(str(next_element))
    print("Question:", task_line.strip())
    return str(correct_answer)
