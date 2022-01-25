#!/usr/bin/env python
from brain_games.scripts import main_logic as ml
from random import randint, choice
from operator import add, sub, mul


def calc():
    operands = {"+": add, "-": sub, "*": mul}
    oper_str = ["+", "-", "*"]
    user = ml.welcome_message()
    counter = 0
    print("What is the result of the expression?")
    while counter < ml.GAME_ROUND:
        calc_game_first_number = randint(1, 10)
        calc_game_second_number = randint(1, 10)
        oper = choice(oper_str)
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
