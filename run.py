# library used to choose a word 
#from a random list of words 
import random 
from colorama import Fore, Style

def welcome_screen():
    """
    Displays welcome message and prompts for user's name.
    Try-except block validates data & raises ValueErrors if incorrect type.
    """
    print("Welcome to Let's see if you can guess it!")
    print("The game is simple, you need to guess the random word letter by letter...")
    print("Did I mention you're given only have 6 attempts?")
    print("I'm sure you can guess it before that...Let's play!")
    print("But first...")
    
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.strip():
                raise ValueError(Fore.RED + "Name cannot be left blank." + Style.RESET_ALL)
            elif not name.isalpha():
                raise ValueError(Fore.RED + "Please only enter letters for your name." + Style.RESET_ALL)
            else:
                print(f'Hi {name}, now we are ready to play!')
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}" + Style.RESET_ALL)
        
welcome_screen()


def select_word():
    """
    Selects a random word from the list.
    """
    words_list = ["lipstick", "popcorn", "daisy", "pretzel", "gingerbread", "girlfriend", "bottle", "lion", "guitar", "sunshine", "music", "coffee", "chair"]
    word = (random.choice(words_list))
    
select_word() 






