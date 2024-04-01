# KM Kamal

# Hangman starter kit
# A program to play the game of hangman
import random

# The main function plays the game and calls other functions
def main():
    words = ['ratatouille',
             'ameliorate',
             'crapulous',
             'supercalifragilisticexpialidocious',
             'bronchitis']

    secret_word = random.choice(words)
    dashes = '-' * len(secret_word)
    print(dashes)

    misses = 10
    while misses > 0:
        letter = get_guess()
        print("You guessed: ", letter)

        if letter in secret_word:
            print(letter, 'is in the word!')
            dashes = update_dashes(secret_word, dashes, letter)
            print(dashes)

            if dashes == secret_word:
                print('Congrats, you won! The secret word was', secret_word + '.')
                break
        else:
            misses -= 1
            print(letter, 'is not in the word!')
            print('You have', misses, 'more tries')

        if misses == 0:
            print('Sorry, you lost.')
            break

    print('Goodbye!')


# Asks the user to guess a letter while making sure user input is
# is a lowercase letter
def get_guess():
    guess = input("Enter a single lowercase letter:  ")
    while guess.isupper() or len(guess) > 1 or guess.isalpha() is False:
        print("Please try again. You must...")
        guess = input("Enter a single lowercase letter:  ")
    return guess


# Updates dashes to match the correct letters guessed
def update_dashes(word, current_dash, ltr):
    for i, j in enumerate(word):
        if j == ltr:
            current_dash = current_dash[:i] + ltr + current_dash[i+1:]
    return current_dash


main()
