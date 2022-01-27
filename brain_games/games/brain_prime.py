#!/usr/bin/env python
from math import sqrt
from random import randint
from brain_games.scripts import main_logic as ml


def is_prime(num):
    """
    функция проверяет словарь prime_dict, сформированный функцией
    check_num на наличие (value.count) ложных значений в словаре

    Parameters
    ----------
    num - число для проверки

    Returns
    -------
    возвращает True если число является простым
    """
    prime_dict = check_num(num)
    for key, value in prime_dict.items():
        if value.count(False) > 0:
            return False
        elif value.count(False) == 0:
            return True


def is_even(num):
    """
    функция проверяет на четность число

    Parameters
    ----------
    num - число для проверки

    Returns
    -------
    возвращает True если четное
    """
    if num % 2 == 0:
        return True
    else:
        return False


def check_num(num):
    """
    функция формирует словарь со списком результатов вычисления по
    критериям простых чисел в диапазоне от 2 до округл. sqrt(num)
    предварительно проверяет на нечетность числа

    Parameters
    ----------
    num - число для проверки

    Returns
    -------
    возвращает словарь ключ-число num, значение-список результатов
    вычисления по критериям простых чисел в булевом типе
    """
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
    """
    функция выводит приветствие, затем задание
    генерирует для этого случайное число (от 2 до 100)
    пока выполняется условие функции guess_number игра продолжается
    в случае ошибки (функция guess_number возвращает False) игра прекращается
    """
    user = ml.welcome_message()
    counter = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while counter < ml.GAME_ROUND:
        prime_game_number = randint(2, 100)
        if ml.guess_number(prime_game_number,
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
