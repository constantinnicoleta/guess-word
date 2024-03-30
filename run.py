# random is a module used to choose a word from a random list of words.
# colorama is a module that allows the colour of text to be changed.
# time module used to pause the execution of the program for the specified number of seconds.
# os module clears the terminal screenn.
import random 
from colorama import Fore, Style
import time
import os

def welcome_screen():
    """
    Displays welcome message and prompts for user's name.
    Try-except block validates data & raises ValueErrors if incorrect type.
    """
    print("Welcome to Let's see if you can guess it!")
    print("\nThe game is simple, you need to guess the random word letter by letter...")
    print("\nDid I mention you're given only have 6 attempts?")
    print("\nI'm sure you can guess it before that...Let's play!")
    print("\nBut first...")
    
    while True:
        try:
            name = input("\nPlease enter your name: ")
            if not name.strip():
                raise ValueError(Fore.RED + "Name cannot be left blank." + Style.RESET_ALL)
            elif not name.isalpha():
                raise ValueError(Fore.RED + "Please only enter letters for your name." + Style.RESET_ALL)
            else:
                print(f'\nHi {name}, now we are ready to play!')
                time.sleep(1)  # Adding a delay of 2 seconds
                os.system('clear')  # Clearing terminal
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}" + Style.RESET_ALL)
        
welcome_screen()


def select_word():
    """
    Selects a random word from the list.
    """
    words_list = ["lipstick", "popcorn", "daisy", "pretzel", "gingerbread", "girlfriend", "bottle", "lion", "guitar", "sunshine", "music", "coffee", "chair"]
    return random.choice(words_list)

    
def display_word(word):
    """Displays the word with blank spaces for each letter to be guessed by user."""
    print("\nWord to guess:")
    for letter in word:
        print(Fore.BLUE + "_", end=" ")  # Print underscore in blue color
    print(Style.RESET_ALL)  # Reset color to default


selected_word = select_word()
guessed_letters = []  # Initialize guessed letters list
display_word(selected_word)

def play_game(word):
    """
    Main game loop where the player guesses letters.
    """
    attempts = 6  # Number of attempts allowed
    guessed_letters = []  # List to store guessed letters
    while attempts > 0:
        print("\nAttempts left:", attempts)
        try:
            guess = input("\nGuess a letter: ").strip().lower()  # Convert input to lowercase and remove leading/trailing spaces
            if not guess:
                raise ValueError("Input cannot be left blank.")
            if len(guess) != 1 or not guess.isalpha():
                if guess.isdigit():
                    raise ValueError("Please enter a letter, not a number.")
                else:
                    raise ValueError("Please enter a single letter.")
        except ValueError as e:
            print(Fore.RED + "Invalid input:", e, Style.RESET_ALL)
            continue  # Skip to next iteration of loop

        guessed_letters.append(guess)  # Add guessed letter to list
        print("Guessed letters:", guessed_letters)  # Print guessed letters for testing purposes
        attempts -= 1  # Decrement attempts for testing purposes

# Test the play_game function with a sample word
play_game("example")