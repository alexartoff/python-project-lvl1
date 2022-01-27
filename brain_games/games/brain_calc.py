#!/usr/bin/env python
from brain_games.scripts import main_logic as ml
from random import randint, choice
from operator import add, sub, mul


def calc():
    """
    функция формирует текстовое выражение expression, которое выводится
    пользователю в виде задания. считает правильный ответ и передаёт
    его функции guess_number
    пока выполняется условие функции guess_number игра продолжается
    в случае ошибки (функция guess_number возвращает False) игра прекращается

    Parameters
    ----------
    operands - словарь математических операндов
    operands_str - список мат.операндов в виде строковых символов
    oper - случайный выбор из списка operands_str
    """
    operands = {"+": add, "-": sub, "*": mul}
    operands_str = ["+", "-", "*"]
    user = ml.welcome_message()
    counter = 0
    print("What is the result of the expression?")
    while counter < ml.GAME_ROUND:
        calc_game_first_number = randint(1, 10)
        calc_game_second_number = randint(1, 10)
        oper = choice(operands_str)
        expression = ("{} {} {}".format(calc_game_first_number,
                                        oper,
                                        calc_game_second_number))
        correct_answer = operands[oper](calc_game_first_number,
                                        calc_game_second_number)
        if ml.guess_number(expression, correct_answer, user, counter):
            counter += 1
        else:
            break


def main():
    calc()


if __name__ == "__main__":
    main()
