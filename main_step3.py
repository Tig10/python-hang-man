#Step 3

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' equal to 6.
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
  display.append('_')

while '_' in display and lives > 0:
  guess = input("Guess a letter: ").lower()

  #Check guessed letter
  for i in range(len(chosen_word)):
    # print(f"Current position: {i}\n Current letter: {chosen_word[i]}\n Guessed letter: {guess}")
    if chosen_word[i] == guess:
      display[i] = guess
    elif guess != chosen_word[i]:
      lives = lives - 1

  #Join all the elements in the list and turn it into a String.
  print(f'{" ".join(display)}')
  
  if lives == 0:
    print('You lose!')
  elif lives > 0 and '_' not in display:
    print('You win!')

#TODO-3: - print all the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
print(stages[lives])