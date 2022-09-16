import random
import string

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
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
from hangman_word_list import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
letter_list=list(string.ascii_letters)
lives = 6
# print(f' the solution is {chosen_word}.')
display = []
for r in range(word_length):
    display += '_'
character_list = []
condition = False
while not condition:
    guess = input("Enter a character: ").lower()
    if len(guess)>1:
        print("You cannot enter more than a letter")
    elif guess not in letter_list:
        print("Try to enter an alphabet")
    else:
        if guess not in character_list:
            if guess in chosen_word:
                for a in range(word_length):
                    letter = chosen_word[a]
                    if guess == letter:
                        display[a] = guess
            else:
                print(f"{guess} is not in the word")
                lives -= 1

            print(''.join(display))
            print(stages[lives])
            if '_' not in display or lives == 0:
                condition = True
        else:
            print("You have already entered this letter before, try something else!")
        character_list += guess
if '_' not in display:
    print("You win")
    input()
elif lives == 0:
    print("You lose")
    input()

