#!/usr/bin/env python
from random import randint, choice
from operator import add, sub, mul


TASK = 'What is the result of the expression?'


def get_question_and_answer():
    """
    функция выполняет арифметические действия над числами a, b

    Returns
    -------
    correct_answer - результат арифметического действия\n
    question - строка-вопрос текущего раунда
    """
    min_number = 1
    max_number = 10
    a = randint(min_number, max_number)
    b = randint(min_number, max_number)
    operators = {"+": add, "-": sub, "*": mul}
    current_operator = choice(list(operators.keys()))
    question = f"{a} {current_operator} {b}"
    correct_answer = operators[current_operator](a, b)
    return str(correct_answer), question
