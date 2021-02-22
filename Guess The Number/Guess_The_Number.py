import random

language = int(input("Do you want the game in \n1. English \n2. Dutch\n"))

if language > 2:
    print("There is no such language")
    exit()
if language < 0:
    print("Verry funny")
    exit()


if language == 1:
    choice = input('Do you want to guess (i) or does the computer(c) have to guess your number: ')
else:
    choice = input('Wil je het nummer raden(i) of moet de computer(c) het nummer raden: ')

if choice == "c":
    print("")

if choice == "i":
    print("")

else:
    quit()

if language == 1:
    hard = int(input('How hard do you want it to be, give a number between 1 and infinity: '))
else: 
    hard = int(input("Hoe hard wil je het maken, kies een nummer tussen 1 en oneindig: "))



if hard < 1:
    if language == 1:
        print(f"Number too low [-_-]")
        exit()
    else:
        print(f"Keuze is te laag [-_-]")
        exit()


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        if language == 1:
            guess = int(input(f'Guess the number between 1 and {x}: '))
            if guess < random_number:
                print('Number too low.')
            elif guess > random_number:
                print('Number too high.')

        if language == 2:
            guess = int(input(f'Kies een nummer tussen 1 en {x}: '))
            if guess < random_number:
                print('Nummer te laag.')
            elif guess > random_number:
                print('Nummer te hoog.')
   
    
    print(f"Je hebt nummer {random_number} geraden en dat was goed")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high

        if language == 1:
            feedback = input(f'Is {guess} too high (h), too low (l), or correct (c)?')
        else:
            feedback = input(f'Is {guess} te hoog (h), te laag (l), of correct (c)?')

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    if language == 1:
        print(f'It is {guess}. Computer know everything')
    else:
        print(f'Het nummer is {guess}. Je computer weet alles')


if choice == 'c':
    computer_guess(hard)

if choice == 'i':
    guess(hard)



