#!/usr/bin/env python
from random import randint
from brain_games.scripts import main_logic as ml


def find_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
            # print(">", a, b)
        else:
            b = b - a
            # print("<", a, b)
    else:
        return a


def gcd():
    user = ml.welcome_message()
    counter = 0
    print('Find the greatest common divisor of given numbers.')
    while counter < ml.GAME_ROUND:
        gcd_game_first_number = randint(1, 100)
        gcd_game_second_number = randint(1, 100)
        game_numbers = ("{} {}".format(gcd_game_first_number,
                                       gcd_game_second_number))
        correct = find_gcd(gcd_game_first_number, gcd_game_second_number)
        if ml.guess_number(game_numbers, correct, user, counter):
            counter += 1
        else:
            break


def main():
    gcd()


if __name__ == "__main__":
    main()
