import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    if user_name:
        print('Hello, {}!'.format(user_name))
    return user_name
