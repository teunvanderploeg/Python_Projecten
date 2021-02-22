import random
import time


language = int(input("Do you want the game in \n1. English \n2. Dutch\n"))

if language > 2:
    print("\nThere is no such language")
    time.sleep(5)
    exit()

if language < 0:
    print("\nVerry funny")
    time.sleep(5)
    exit()


if language == 1:
    choice = input('Do you want to guess (i) or does the computer(c) have to guess your number: ')
else:
    choice = input('Wil je het nummer raden(i) of moet de computer(c) het nummer raden: ')

if choice == "c":
    print("")

elif choice == "i":
    print("")

else:
    print("\nDat was geen i of c!")
    time.sleep(5)
    exit()

if language == 1:
    hard = int(input('How hard do you want it to be, give a number between 1 and infinity: '))
else: 
    hard = int(input("Hoe hard wil je het maken, kies een nummer tussen 1 en oneindig: "))



if hard < 1:
    if language == 1:
        print(f"\nNumber too low [-_-]")
        time.sleep(5)
        exit()
    else:
        print(f"\nKeuze is te laag [-_-]")
        time.sleep(5)
        exit()


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    kies = 0


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
        kies += 1
   
    
    print(f"\nJe hebt nummer {random_number} geraden en dat was goed. Je hebt het geraden in {kies} keer")
    time.sleep(5)

def computer_guess(x):
    low = 1
    kies = 0
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
        kies += 1

    if language == 1:
        print(f'\nIt is {guess}. And in {kies} guesses. Computer know everything')
        time.sleep(5)

    else:
        print(f'\nHet nummer is {guess}. En in {kies} keuzes. Je computer weet alles')
        time.sleep(5)


if choice == 'c':
    computer_guess(hard)

if choice == 'i':
    guess(hard)



