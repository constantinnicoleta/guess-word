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
            name = input("\nPlease enter your name: ")
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
                time.sleep(1)  # Adding a delay of 1 second
                os.system('clear')  # Clearing terminal
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}" + Style.RESET_ALL)


def select_word():
    """Select a random word from the list."""

    words_list = ["lipstick", "popcorn", "daisy", "pretzel",
                  "gingerbread", "girlfriend", "bottle", "lion",
                  "guitar", "sunshine", "music", "coffee", "chair"]
    return random.choice(words_list)  # returns random word from list


def display_word(word, guessed_letters):
    """
    Display the word with blank spaces.
    for each letter to be guessed by user.
    """

    print("\nWord to guess:")
    for letter in word:
        print(Fore.BLUE + "_", end=" ")  # Print underscore in blue color
    print(Style.RESET_ALL)  # Reset color to default


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
    attempts = 6  # Number of attempts allowed
    guessed_letters = []  # List to store guessed letters
    while attempts > 0:
        print("\nAttempts left:", attempts)
        try:
            # Convert input to lowercase and remove leading/trailing spaces
            guess = input("\nGuess a letter: ").strip().lower()
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
            continue  # Skip to next iteration of loop

        if guess in guessed_letters:
            # player informed they've already guessed a particular letter
            print(Fore.YELLOW +
                  "You've already guessed this letter." + Style.RESET_ALL)
            display_word_with_guesses(word, guessed_letters)
            continue

        guessed_letters.append(guess)  # adding the guessed letter to the list

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
            os.system('clear')  # Clears the terminal screen
            print(displayed_word)
            # informs player they've guessed the word
            print(Fore.BLUE +
                  "Congratulations! You've guessed the word!" +
                  Style.RESET_ALL)
            break  # exit the loop if condition met
        elif attempts == 0:
            # informs player they ran out of attempts
            print(Fore.RED + "Out of attempts! The word was:", word +
                  Style.RESET_ALL)

    while True:
        # asks the player if want to play again
        decision = input("Do you want to play again? (y/n)").strip().lower()
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

    display = ""  # empty string to hold the displayed word
    for letter in word:
        if letter in guessed_letters:  # checks if the letter has been guessed
            display += letter + " "  # adds it to display sting if guessed
        else:
            display += "_ "  # displaying underscore and hidded if not guessed
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
