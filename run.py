import random
from colorama import Fore, Style
import time
import os


def welcome_screen():
    """
    Display welcome message and prompts for user's name.

    Try-except block validate data & raise ValueErrors if incorrect type.
    """
    print("Welcome to Let's see if you can guess it!")
    print("\nThe game is simple:")
    print("\nYou need to guess the random word letter by letter")
    print("\nDid I mention you're given only have 6 attempts?")
    print("\nI'm sure you can guess it before that...Let's play!")
    print("\nBut first...")

    while True:
        try:
            name = input("\nPlease enter your name:\n")
            if not name.strip():
                # validate user input
                raise ValueError(
                      Fore.RED + "Name cannot be left blank." +
                      Style.RESET_ALL)
            elif not name.isalpha():
                # validate user input
                raise ValueError(Fore.RED +
                      "Please only enter letters for your name." +
                                 Style.RESET_ALL)
            else:
                print(f'\nHi {name}, now we are ready to play!')
                # Adding a delay of 1 second
                time.sleep(1)
                # Clearing terminal
                os.system('clear')
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}" + Style.RESET_ALL)


def select_word():
    """Select a random word from the list."""

    words_list = ["lipstick", "popcorn", "daisy", "pretzel",
                  "gingerbread", "girlfriend", "bottle", "lion",
                  "guitar", "sunshine", "music", "coffee", "chair"]
    # returns random word from list
    return random.choice(words_list)


def display_word(word, guessed_letters):
    """
    Display the word with blank spaces.
    for each letter to be guessed by user.
    """

    print("\nWord to guess:")
    for letter in word:
        # Print underscore in blue color
        print(Fore.BLUE + "_", end=" ")
        # Reset color to default
    print(Style.RESET_ALL)


def play_game(word):
    """
    Game loop where the player guesses letters.
    Used while loop, condition and if statements.
    Validate user input
    Inform player if the letter is correct/incorrect/already guessed.
    Shows current state of word as the letter guessing.
    Inform player they guessed the word or
    Inform player they ran out of attempts if all attempts used.
    """
    # Number of attempts allowed
    attempts = 6
    # List to store guessed letters
    guessed_letters = []
    while attempts > 0:
        print("\nAttempts left:", attempts)
        try:
            # Convert input to lowercase and remove leading/trailing spaces
            guess = input("\nGuess a letter:\n ").strip().lower()
            if not guess:
                # validate user input
                raise ValueError("Input cannot be left blank.")
            if len(guess) != 1 or not guess.isalpha():
                if guess.isdigit():
                    # validate user input
                    raise ValueError("Please enter a letter, not a number.")
                else:
                    # validate user input
                    raise ValueError("Please enter a single letter.")
        except ValueError as e:
            print(Fore.RED + "Invalid input:", e, Style.RESET_ALL)
            # skip to next iteration of loop
            continue

        if guess in guessed_letters:
            # player informed they've already guessed a particular letter
            print(Fore.YELLOW +
                  "You've already guessed this letter." + Style.RESET_ALL)
            display_word_with_guesses(word, guessed_letters)
            continue
        # adding the guessed letter to the list
        guessed_letters.append(guess)

        if guess in word:
            # informs player the letter guessed is correct
            print(Fore.GREEN + "Correct guess!" + Style.RESET_ALL)
        else:
            attempts -= 1
            # informs player the letter guessed is incorrect
            print(Fore.RED + "Incorrect guess!" + Style.RESET_ALL)
            # shows current state of words with letters guessed
        displayed_word = display_word_with_guesses(word, guessed_letters)

        if "_" not in displayed_word:
            # Clears the terminal screen
            os.system('clear')
            print(displayed_word)
            # informs player they've guessed the word
            print(Fore.BLUE +
                  "Congratulations! You've guessed the word!" +
                  Style.RESET_ALL)
            # exit the loop if condition met
            break
        elif attempts == 0:
            # informs player they ran out of attempts
            print(Fore.RED + "Out of attempts! The word was:", word +
                  Style.RESET_ALL)

    while True:
        # asks the player if want to play again
        decision = input("Do you want to play again? (y/n)\n").strip().lower()
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print(Fore.RED +
                  "Invalid input! Please enter 'y' to replay or 'n' to quit." +
                  Style.RESET_ALL)


def display_word_with_guesses(word, guessed_letters):
    """
    Display the word with all the correct guessed letters filled in.
    Display the incorrect guesses.
    """
    # empty string to hold the displayed word
    display = ""
    for letter in word:
        # checks if the letter has been guessed
        if letter in guessed_letters:
            # adds it to display sting if guessed
            display += letter + " "
        else:
            # displaying underscore and hidded if not guessed
            display += "_ "
    print(display)

    # Display incorrect guesses
    # iterates through each letter to check if that letter is not in the word
    incorrect_guesses = [
         letter for letter in guessed_letters if letter not in word]
    if incorrect_guesses:
        print("\nIncorrect guesses:", ", ".join(incorrect_guesses))
    return display


def main():
    """
    Main function which holds all the functions.
    Play again option for user.
    """

    welcome_screen()
    replay = True
    while replay is True:
        selected_word = select_word()
        guessed_letters = []
        display_word(selected_word, guessed_letters)
        replay = play_game(selected_word)

        # if user selects 'y', will clear prev terminal screen & play again
        if replay is True:
            os.system('clear')
        else:
            # if user selected 'n' will end game and display message
            print("Thank you for playing! Goodbye :).")


main()
