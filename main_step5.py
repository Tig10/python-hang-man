# main_step5.py
# Step 5

import random
import hangman_art
import hangman_words

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line word_list = ['aardvark', 'baboon', 'camel']

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

end_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game
print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for letter in chosen_word:
    display.append('_')

while not end_game:
    guess = input('Guess a letter: ').lower()

    # TODO-4: If the user has entered a letter they've already guessed, print the letter and let them know
    if guess in display:
        print(f'You have already guessed the letter "{guess}"')

    # Check guessed letter
    for i in range(len(chosen_word)):
        # print(f'Current postion: {i}\nCurrent letter: {chosen_word[i]}\nGuessed letter: {guess}')
        if guess == chosen_word[i]:
            display[i] = guess

    # Check if user is wrong
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the
        #  chosen_word
        print(f'"{guess}" is not the chosen word, please try a different word.')
        lives -= 1
        if lives == 0:
            end_game = True
            print('You lose')
            print(f'The word is {chosen_word}')

    # Join all the elements in list and turn it into a String.
    print(f'{" ".join(display)}')

    if '_' not in display:
        end_game = True
        print('You win!')

    # TODO-3: - print all the ASCII art from 'stages' that correspond to the current number of 'lives' the user has
    #  remaining.
    stages = hangman_art.stages
    print(stages[lives])
