import random
import sys


#list of words matching levels for the game

with open("words.txt") as words_file:
    
    easy_mode = [word.strip()
    for word in words_file.readlines()
    if len(word)>=4 and len(word)<=6]

with open("words.txt") as words_file:

    normal_mode = [word.strip()
    for word in words_file.readlines()
    if len(word)>=6 and len(word)<=8]

with open("words.txt") as words_file:

    hard_mode = [word.strip()
    for word in words_file.readlines()
    if len (word)>=8]

# program function
def pick_diff():
    """let player pick and confirm a difficulty level."""
    prompt = "Please select a difficulty.  (easy, normal, hard)\n>"
    choice = "" 
    while choice not in ['easy', 'normal', 'hard'] :
        choice = input(prompt)
        choice = choice.lower()
    change_diff(choice)

def change_diff(level):
    """allow the player a chance to change difficulty."""
    message = "\nyou picked " + level + ". Do you want to change level? [Y/N]\n>"
    answer = input(message).lower()
    while answer not in ['y', 'n']:
        answer = input (message). lower()
    if answer == 'y':
        pick_diff()
    if answer == 'n':
        print("\nReady to play\n")
        choose_word(level)

def choose_word(choice):
    """assign the game word based on the player difficulty choice."""
    if choice == 'easy':
        word = random.choice(easy_mode)
    elif choice == 'normal':
        word = random.choice(normal_mode)
    elif choice == 'hard':
        word = random.choice(hard_mode)
    play_game(word)

def play_game(this_word):
    """run the game."""
    word = list(this_word)
    blanks = list("_ " * len(word))
    guessed = []
    incorrect = 8
    while incorrect > 0:
        print("you have {} chances left.".format(incorrect)) 
        print("your word: ")
        blank = ""
        join_text = blank.join(blanks)
        print(join_text)
        print("guessed letters: ") 
        print(" , ".join(guessed))

        letter = input("your guess:").lower()
        if len (letter) ==1 and letter.isalpha():
            if letter in guessed:
                print("\n\nHey you already guessed that")
            elif letter in word:
                for index, character in enumerate(word):
                    blanks = list(blanks)
                    if character == letter:
                        blanks [index] = letter
                        if blanks == word:
                            print("\n\nwinner" + "\nyour word was " + ''.join(word) + ".\n")
                            play_again()
            elif letter not in word:
                incorrect -= 1
                guessed.append(letter)
            else:
                print("\n\n!input invalid only single letters allowed !\n\n")
        else:
            print("\nsorry " + player + ", game over\nyour word was " + ''.join(word) + ".")

# Introduction, explanation of game.
player = input("lets play mystery word! ")
print("\nhey, " + player + " !\nyou get 8 incorrect guesses before you lose."
      "\nwhich difficulty would you like?"
      "\n easy_mode"
      "\n normal_mode"
      "\n hard_mode")

# Choose difficulty and begin
difficulty = pick_diff()




       












