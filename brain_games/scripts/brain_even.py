#!/usr/bin/env python
from brain_games import cli
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 3
    correct = ''
    while counter != 0:
        guess_number = randint(1, 100)
        print("Question:", guess_number)
        answer = input("Your answer: ")
        if guess_number % 2 == 0 and answer == 'yes':
            print("Correct!")
            counter -= 1
        elif guess_number % 2 == 1 and answer == 'no':
            print("Correct!")
            counter -= 1
        else:
            if answer == 'yes':
                correct = 'no'
            elif answer == 'no':
                correct == 'yes'
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\
                ".format(answer, correct))
            print("Let's try again, {}!".format(name))
            break
    if counter == 0:
        print("Congratulations, {}!".format(name))


def main():
    even()


if __name__ == "__main__":
    main()
