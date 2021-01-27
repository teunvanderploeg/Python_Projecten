import random
import string
from words import words
import os


def clear(): return os.system('cls')


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    error = ''

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        clear()
        print('Guess the English word, in this game of Hangman')
        print(error)
        error = ''
        print("Lives left: ", lives)
        print("letter used, ", ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1

        elif user_letter in used_letters:
            print('You already used that character. Please try again.')
        else:
            print('Invalid character. Try again')
            error = 'Invalid character. Try again'
    if lives == 0:
        print("You're dead... :(")
        print('You word was', word, ".")
    else:
        print('You guessed the word', word, "!! :)")


clear()
hangman()
