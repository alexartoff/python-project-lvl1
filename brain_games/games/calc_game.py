#!/usr/bin/env python


def calculate(a, b, operand):
    """
    функция выполняет арифмитические действия над часлами a, b
    Parameters
    ----------
    a - число\n
    b - число\n
    operand - арифметический оператор

    Returns
    -------
    answer - результат арифметического действия
    """
    answer = operand(a, b)
    return answer
