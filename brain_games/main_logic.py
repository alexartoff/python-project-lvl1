import prompt


def lets_play(game):
    """
    Функция выводит приветствие, получает имя пользователя,
    запускает выбранную пользователем игру и включает счетчик раундов

    Parameters
    ----------
    game - получение данных из вызываемой игры таких как:\n
    \tконстанта TASK и передача её в функцию welcome_message()\n
    \tget_data_from_game - получение tuple содержащего:
    \t\tправильный ответ (для последующей проверки)\n
    \t\tстроку-задание для текущего раунда
    """
    user_name = prompt.string('Welcome to the Brain Games!\n\
May I have your name? ')
    print(f"Hello, {user_name}!\n{game.TASK}")
    rounds_count = 1
    game_rounds = 3
    while rounds_count <= game_rounds:
        correct, question = game.get_data_from_game()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        # NOTE - хотел использовать словарь с вариантами ответов, но после
        # просмотра видосов Кирилла закрались сомнения - а стоит ли?
        # Так как получилось сейчас не нравится вывод сообщения о проигрыше -
        # режет глаз такая конструкция, но зато строк кода меньше
        if user_answer == correct:
            print("Correct!")
            rounds_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct}'.\nLet's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
