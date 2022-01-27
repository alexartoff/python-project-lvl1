#!/usr/bin/env python
from random import randint
from brain_games.scripts import main_logic as ml


def arfm_progr():
    """
    функция выводит приветствие, затем задание
    формирует арифметическую прогрессию произвольной длины (от 5 до 10)
    с произвольно пропущенным элементом (не крайним)
    пока выполняется условие функции guess_number игра продолжается
    в случае ошибки (функция guess_number возвращает False) игра прекращается
    """
    user = ml.welcome_message()
    counter = 0
    print('What number is missing in the progression?')
    while counter < ml.GAME_ROUND:
        element_count = randint(5, 10)
        first_element = randint(1, 10)
        iterator = randint(1, 10)
        skip_element = randint(2, (element_count - 1))
        output = "{} ".format(str(first_element))
        next_element = first_element

        for i in range(1, element_count):
            next_element += iterator
            if i == skip_element:
                output += ".. "
                correct_answer = next_element
            else:
                output += "{} ".format(str(next_element))
        if ml.guess_number(output.strip(), correct_answer, user, counter):
            counter += 1
        else:
            break


def main():
    arfm_progr()


if __name__ == "__main__":
    main()
