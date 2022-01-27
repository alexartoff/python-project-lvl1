#!/usr/bin/env python
from math import sqrt
from random import randint
from brain_games.scripts import main_logic as ml


def is_prime(num):
    prime_dict = check_num(num)
    for key, value in prime_dict.items():
        if value.count(False) > 0:
            return False
        elif value.count(False) == 0:
            return True


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def check_num(num):
    out = {}
    val = []
    if not is_even(num):
        for i in range(2, round(sqrt(num))):
            if num % i >= 1 and num > i:
                val.append(True)
            elif num % i == 0 and num > i:
                val.append(False)
        out[num] = val
    return out


def prime():
    user = ml.welcome_message()
    counter = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter < ml.GAME_ROUND:
        prime_game_number = randint(2, 100)
        if ml.guess_number_yes(prime_game_number,
                               is_prime(prime_game_number),
                               user,
                               counter):
            counter += 1
        else:
            break


def main():
    prime()


if __name__ == "__main__":
    main()
