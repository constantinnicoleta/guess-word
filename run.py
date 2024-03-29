# library used to choose a word 
#from a random list of words 
import random 

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
                raise ValueError("Name cannot be left blank.")
            elif not name.isalpha():
                raise ValueError("Please only enter letters for your name.")
            else:
                print(f'Hi {name}, now we are ready to play!')
                break
        except ValueError as e:
            print(f"Invalid input: {e}")
        
welcome_screen()


  
    