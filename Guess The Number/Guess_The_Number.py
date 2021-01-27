import random

choice = input(
    'Do you want to guess (i) or does the computer(c) have to guess your number: ')
hard = int(
    input('how hard do you want it to be give a number between 1 and infinity}: '))
if hard < 1:
    print(f"Too low number [-_-]")
    exit()


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < random_number:
            print('Number too low.')
        elif guess > random_number:
            print('Number too high.')
    print(f"You have guessed the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(
            f'Is {guess} too high (h), too low (l), or correct (c)?')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'It is {guess}. Computer know everything')


if choice == 'c':
    computer_guess(hard)
else:
    guess(hard)
