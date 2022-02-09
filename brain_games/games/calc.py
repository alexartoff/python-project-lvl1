#!/usr/bin/env python
from random import randint, choice
from operator import add, sub, mul


TASK = 'What is the result of the expression?'


def game_mechanics():
    """
    функция выполняет арифмитические действия над часлами a, b

    Returns
    -------
    answer - результат арифметического действия\n
    question - строка-задание текущего раунда
    """
    a = randint(1, 10)
    b = randint(1, 10)
    operands = {"+": add, "-": sub, "*": mul}
    operands_str = ["+", "-", "*"]
    oper = choice(operands_str)
    question = f"{a} {oper} {b}"
    correct_answer = operands[oper](a, b)
    return str(correct_answer), question
