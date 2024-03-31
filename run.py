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
                raise ValueError(Fore.RED + "Name cannot be left blank." + Style.RESET_ALL) #validate user input
            elif not name.isalpha():
                raise ValueError(Fore.RED + "Please only enter letters for your name." + Style.RESET_ALL) #validate user input
            else:
                print(f'\nHi {name}, now we are ready to play!')
                time.sleep(1)  # Adding a delay of 2 seconds
                os.system('clear')  # Clearing terminal
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}" + Style.RESET_ALL)
        


def select_word():
    """
    Selects a random word from the list.
    """
    words_list = ["lipstick", "popcorn", "daisy", "pretzel", "gingerbread", "girlfriend", "bottle", "lion", "guitar", "sunshine", "music", "coffee", "chair"]
    return random.choice(words_list) #returns random word from list

    
def display_word(word,guessed_letters):
    """
    Displays the word with blank spaces for each letter to be guessed by user.
    """
    print("\nWord to guess:")
    for letter in word:
        print(Fore.BLUE + "_", end=" ")  # Print underscore in blue color
    print(Style.RESET_ALL)  # Reset color to default

def play_game(word):
    """
    Main game loop where the player guesses letters using while loop, condition and if statements.
    Validate user input, informs player if the letter is correct/incorrect/already guessed.
    Shows current state of word as the letter guessing.
    Informs player they guessed the word or
    Informs player they ran out of attempts if all attempts used.
    
    """
    
    attempts = 6  # Number of attempts allowed
    guessed_letters = []  # List to store guessed letters
    while attempts > 0:
        print("\nAttempts left:", attempts)
        try:
            guess = input("\nGuess a letter: ").strip().lower()  # Convert input to lowercase and remove leading/trailing spaces
            if not guess:
                raise ValueError("Input cannot be left blank.") #validate user input
            if len(guess) != 1 or not guess.isalpha():
                if guess.isdigit():
                    raise ValueError("Please enter a letter, not a number.") #validate user input
                else:
                    raise ValueError("Please enter a single letter.") #validate user input
        except ValueError as e:
            print(Fore.RED + "Invalid input:", e, Style.RESET_ALL)
            continue  # Skip to next iteration of loop

        if guess in guessed_letters:
            print(Fore.YELLOW + "You've already guessed this letter." + Style.RESET_ALL) #informs the player that they've already guessed a particular letter 
            display_word_with_guesses(word, guessed_letters) 
            continue  

        guessed_letters.append(guess) #adding the guessed letter to the list

        if guess in word:
            print(Fore.GREEN + "Correct guess!" + Style.RESET_ALL) #informs player the letter guessed is correct
        else:
            attempts -= 1
            print(Fore.RED + "Incorrect guess!" + Style.RESET_ALL)#informs player the letter guessed is incorrect
        displayed_word = display_word_with_guesses(word, guessed_letters) #shows current state of words with letters guessed

        if "_" not in displayed_word:
            os.system('clear')  # Clears the terminal screen
            print(displayed_word)
            print(Fore.BLUE + "Congratulations! You've guessed the word!" + Style.RESET_ALL) #informs player they've guessed the word
            break #exit the loop if condition met
        elif attempts == 0:
            print(Fore.RED + "Out of attempts! The word was:", word + Style.RESET_ALL) #informs player they ran out of attempts

    while True:
        decision = input("Do you want to play again? (y/n)").strip().lower() # asks the player if want to play again
        if decision == "y": 
            return True
        elif decision == "n":
            return False
        else:
            print(Fore.RED + "Invalid input! Please enter 'y' to play again or 'n' to quit."+ Style.RESET_ALL)


def display_word_with_guesses(word, guessed_letters):
    """
    Displays the word with all the correct guessed letters filled in and also displays the incorrect guesses.
    """
    display = "" #empty string to hold the displayed word
    for letter in word:
        if letter in guessed_letters: #checks if the letter has been guessed
            display += letter + " "  #adds it to display sting if guessed
        else:
            display += "_ " #displaying underscore and hidded if not guessed
    print(display)

    # Display incorrect guesses
    incorrect_guesses = [letter for letter in guessed_letters if letter not in word] #iterates through each letter to check if that letter is not in the variable word.
    if incorrect_guesses:
        print("\nIncorrect guesses:", ", ".join(incorrect_guesses))
    return display    


def main():
    welcome_screen()
    replay = True;
    while replay == True:
        selected_word = select_word()
        guessed_letters = [] 
        display_word(selected_word,guessed_letters)
        replay = play_game(selected_word) 

        if replay == True: # if user selects 'y', will clear prev terminal screen & play again 
            os.system('clear')
        else:
            print("Thank you for playing! Goodbye :).") # if user selected 'n' will end game and display message

main()
     
           