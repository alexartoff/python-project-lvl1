from brain_games.games import brain_even as be
import prompt


GAME_ROUND = 3
user_name = 'none'


def welcome_message():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {}!'.format(user_name))
        return user_name


def guess_number(game_number, user, counter):
    print("Question:", game_number)
    answer = input("Your answer: ")
    if check_answer(answer, be.is_even(game_number), user, counter):
        return True
    else:
        return False


def guess_number_calc(game_number, correct, user, counter):
    print("Question:", game_number)
    answer = input("Your answer: ")
    if check_answer_calc(answer, correct, user, counter):
        return True
    else:
        return False


def anti_answer(ans):
    if ans == 'yes':
        return 'no'
    elif ans == 'no':
        return 'yes'


def check_answer(ans, cor_bl, user, counter):
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


def check_answer_calc(ans, cor, user, counter):
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
