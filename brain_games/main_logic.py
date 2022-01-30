import prompt


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


def start_game(game_task, get_correct_answer):
    """
    Функция выводит приветствие, получает имя пользователя,
    запускает выбранную пользователем игру и включает счетчик раундов\n
    правильный ответ передаётся в функцию check_ans(), которая после проверки
    возвращает True/False

    Parameters
    ----------
    game_task - вывод описания задания игры\n
    get_correct_answer - получение правильного ответа для последующей
    передачи на проверку
    """
    user_name = welcome_message()
    print(game_task)
    counter = 1
    while counter <= GAME_ROUND:
        correct = get_correct_answer()
        if check_ans(correct, user_name):
            counter += 1
        else:
            break
    else:
        print("Congratulations, {}!".format(user_name))


def check_ans(correct, user_name):
    """
    Функция проверяет ответ игрока и выводит соотвествующее сообщение

    Parameters
    ----------
    correct - получение правильного ответа для проверки\n
    user_name - имя пользователя

    Returns
    -------
    возвращает True/False
    """
    answer = prompt.string('Your answer: ')
    if answer == correct:
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n\
Let's try again, {}!".format(answer, correct, user_name))
        return False
