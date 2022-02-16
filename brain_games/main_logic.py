import prompt


def run_game(game):
    """
    Функция выводит приветствие, получает имя пользователя,
    запускает выбранную пользователем игру и включает счетчик раундов

    Parameters
    ----------
    game - получение данных из вызываемой игры таких как:\n
    \tконстанта TASK с последующим выводом задания на экран\n
    \tget_question_and_answer - получение tuple содержащего:
    \t\tправильный ответ (для последующей проверки)\n
    \t\tстроку-вопрос для текущего раунда
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!\n"
          f"{game.TASK}")
    rounds_count = 1
    game_rounds = 3
    while rounds_count <= game_rounds:
        correct, question = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct:
            print("Correct!")
            rounds_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct}'.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
