import prompt


GAME_ROUND = 3
WELCOME = 'Welcome to the Brain Games!'


def welcome_message(game_task):
    """
    функция вывода приветствия, описания задания игры и
    запроса имени пользователя в переменную user_name

    Parameters
    ----------
    game_task - получение описания задания игры

    Returns
    -------
    возвращает имя пользователя
    """
    user_name = prompt.string(f'{WELCOME}\nMay I have your name? ')
    print(f"Hello, {user_name}!\n{game_task}")
    return user_name


def start_game(game):
    """
    Функция выводит приветствие, получает имя пользователя,
    запускает выбранную пользователем игру и включает счетчик раундов

    Parameters
    ----------
    game - получение данных из вызываемой игры таких как:\n
    \tконстанта TASK и передача её в функцию welcome_message()\n
    \tgame_mechanics - получение tuple содержащего:
    \t\tправильный ответ (для последующей проверки)\n
    \t\tстроку-задание для текущего раунда
    """
    user_name = welcome_message(game.TASK)
    counter = 1
    while counter <= GAME_ROUND:
        correct, question = game.game_mechanics()
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == correct:
            result_message(answer, correct, user_name, "correct")
            counter += 1
        else:
            result_message(answer, correct, user_name, "lose")
            break
    else:
        result_message(answer, correct, user_name, "win")


def result_message(answer, correct, user_name, round_result):
    """
    Функция выводит результаты игры

    Parameters
    ----------
    answer - ответ игрока\n
    correct - правильный ответ\n
    user_name - имя игрока\n
    round_result - результат проверки на правильность в раунде
    """
    game_results_dict = {
        "correct": "Correct!",
        "win": f"Congratulations, {user_name}!",
        "lose": f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct}'.\nLet's try again, {user_name}!"
    }
    print(f'{game_results_dict[round_result]}')
