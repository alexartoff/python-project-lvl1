import prompt


GAME_ROUND = 3
user_name = 'none'


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


def guess_number(game_number, correct, user, counter):
    """
    функция выводит пользователю вопрос в зависимости от запущенной игры

    Parameters
    ----------
    game_number - вывод задания
    correct - правильный ответ
    user - имя пользователя (передаётся дальше в функцию check_answer)
    counter - счетчик раундов (передаётся дальше в функцию check_answer)

    Returns
    -------
    возвращает результат проверки правильности введенного ответа
    для дальнейшего продолжени игры
    """
    print("Question:", game_number)
    answer = input("Your answer: ")
    if answer == "yes" or answer == "no":
        if check_answer_yes(answer, correct, user, counter):
            return True
        else:
            return False
    else:
        if check_answer(answer, correct, user, counter):
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


def check_answer_yes(ans, cor_bl, user, counter):
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
            print("Correct!\nCongratulations, {}!".format(user))
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\
            ".format(ans, anti_answer(ans)))
        print("Let's try again, {}!".format(user))
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
