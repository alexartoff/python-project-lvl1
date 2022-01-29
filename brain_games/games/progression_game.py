#!/usr/bin/env python
from random import randint


def progression(first, count, step):
    """
    формирует арифметическую прогрессию произвольной длины (от 5 до 10)
    с произвольно пропущенным элементом (не крайним)

    Parameters
    ----------
    first - первое число прогрессии\n
    count - количество элементов прогрессии\n
    step - шаг прогрессии

    Returns
    -------
    возвращает строку арифметической прогрессии с пропущенным элементом
    и сам элемент
    """
    skip = randint(2, (count - 2))
    out_line = "{} ".format(str(first))
    next_el = first
    for i in range(1, count):
        next_el += step
        if i == skip:
            out_line += ".. "
            correct_answer = next_el
        else:
            out_line += "{} ".format(str(next_el))
    return (out_line.strip(), correct_answer)
