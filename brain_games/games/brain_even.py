#!/usr/bin/env python
from random import randint
from brain_games.scripts import main_logic as ml


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def even_refactor():
    user = ml.welcome_message()
    counter = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < ml.GAME_ROUND:
        even_game_number = randint(1, 100)
        if ml.guess_number_yes(even_game_number,
                               is_even(even_game_number),
                               user,
                               counter):
            counter += 1
        else:
            break


def main():
    even_refactor()


if __name__ == "__main__":
    main()
