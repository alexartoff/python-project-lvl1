import prompt
from random import randint, choice
from brain_games.games import even_game as evn
from brain_games.games import gcd_game as gcd
from brain_games.games import calc_game as clc
from brain_games.games import progression_game as prgrs
from brain_games.games import prime_game as prm
from operator import add, sub, mul


GAME_ROUND = 3


def welcome_message():
    """
    функция вывода приветствия
    запроса имени пользователя в переменную user_name

    Returns
    -------
    возвращает имя пользователя
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {}!'.format(user_name))
        return user_name


def guess_number(game_task, correct, user_name, counter):
    """
    функция выводит пользователю вопрос в зависимости от запущенной игры

    Parameters
    ----------
    game_task - вывод задания
    correct - правильный ответ
    user - имя пользователя (передаётся дальше в функцию check_answer)
    counter - счетчик раундов (передаётся дальше в функцию check_answer)

    Returns
    -------
    возвращает результат проверки правильности введенного ответа
    для дальнейшего продолжени игры
    """
    print("Question:", game_task)
    answer = prompt.string('Your answer: ')
    if answer == "yes" or answer == "no":
        if check_answer_yes(answer, correct, user_name, counter):
            return True
        else:
            return False
    else:
        if check_answer(answer, correct, user_name, counter):
            return True
        else:
            return False


def anti_answer(ans):
    """
    функция инвертирует ответ при выводе текста ошибки

    Parameters
    ----------
    ans - ответ, который нужно инвертировать

    Returns
    -------
    возвращает инвертированный ответ
    """
    if ans == 'yes':
        return 'no'
    elif ans == 'no':
        return 'yes'


def check_answer_yes(ans, cor_bl, user_name, counter):
    """
    функция проверки правильности введенного пользователем текстового ответа

    Parameters
    ----------
    ans - введенный ответ
    cor_bl - правильный ответ в булевом типе (bool)
    user - имя пользователя
    counter - счетчик раундов

    Returns
    -------
    возвращает результат проверки в булевом типе
    и выводит соответствующие сообщения пользователю на экран
    """
    if (ans == 'yes' and cor_bl) or (ans == 'no' and not cor_bl):
        if counter < 2:
            print("Correct!")
        else:
            print("Correct!\nCongratulations, {}!".format(user_name))
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
            ".format(ans, anti_answer(ans)))
        print("Let's try again, {}!".format(user_name))
        return False


def check_answer(ans, cor, user, counter):
    """
    функция проверки правильности введенного пользователем числового ответа

    Parameters
    ----------
    ans - введенный ответ
    cor - правильный ответ в числовом типе (int)
    user - имя пользователя
    counter - счетчик раундов

    Returns
    -------
    возвращает результат проверки в булевом типе
    и выводит соответствующие сообщения пользователю на экран
    """
    if int(ans) == cor:
        if counter < 2:
            print("Correct!")
        else:
            print("Correct!\nCongratulations, {}!".format(user))
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
            ".format(ans, cor))
        print("Let's try again, {}!".format(user))
        return False


def start_game(game_name, user_name):
    counter = 0
    operands = {"+": add, "-": sub, "*": mul}
    operands_str = ["+", "-", "*"]
    while counter < GAME_ROUND:
        if game_name == 'even':
            game_task = randint(1, 100)
            correct_answer = evn.is_even(game_task)
        elif game_name == 'calc':
            first = randint(1, 10)
            second = randint(1, 10)
            oper = choice(operands_str)
            game_task = ("{} {} {}".format(first,
                                           oper,
                                           second))
            correct_answer = clc.calculate(first,
                                           second,
                                           operands[oper])
        elif game_name == 'gcd':
            first = randint(1, 100)
            second = randint(1, 100)
            game_task = ("{} {}".format(first, second))
            correct_answer = gcd.find_gcd(first, second)
        elif game_name == 'prime':
            game_task = randint(1, 100)
            correct_answer = prm.is_prime(game_task)
        elif game_name == 'progression':
            first = randint(1, 10)
            count = randint(5, 10)
            step = randint(1, 10)
            (game_task, correct_answer) = prgrs.progression(first, count, step)
        if guess_number(game_task, correct_answer, user_name, counter):
            counter += 1
        else:
            break
