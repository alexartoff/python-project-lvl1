#!/usr/bin/env python
from random import randint, choice
from operator import add, sub, mul


def calculate():
    """
    функция выполняет арифмитические действия над часлами a, b

    Returns
    -------
    answer - результат арифметического действия
    """
    a = randint(1, 10)
    b = randint(1, 10)
    operands = {"+": add, "-": sub, "*": mul}
    operands_str = ["+", "-", "*"]
    oper = choice(operands_str)
    task = ("{} {} {}".format(a, oper, b))
    print("Question:", task)
    correct_answer = operands[oper](a, b)
    return str(correct_answer)
