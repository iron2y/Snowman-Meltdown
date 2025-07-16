import random
from encodings.rot_13 import rot13

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_NUMBER_OF_MISTAKES = 3


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def create_word_hint(secret_word, guessed_letters):
    """Creates a word hint based on the secret word."""
    if guessed_letters:
        hidden_word = ""
        for char in secret_word:
            if char in guessed_letters:
                hidden_word += char
            else:
                hidden_word += "_"
    else:
        hidden_word = "_" * len(secret_word)
    return " ".join(hidden_word)


def display_game_state(mistakes, secret_word, guessed_letters, state=""):
    """Displays the current game state."""
    print(STAGES[mistakes])
    if state == "lost":
        print(f"\033[33mGame Over! The word was: {secret_word}\033[0m")
        return None
    elif state == "won":
        print(f"\033[33mCongratulations, you saved the snowman!\nYou guessed the word: {secret_word}\033[0m")
        return None
    hidden_word = create_word_hint(secret_word, guessed_letters)
    print(f"Word: {hidden_word}")
    return None


def is_valid_input(guess):
    """Checks if the input is a valid letter."""
    return len(guess) == 1 and guess.isalpha()


def play_game():
    secret_word = get_random_word()
    print("\033[33m\nWelcome to Snowman Meltdown!\033[0m")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = set()
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        while True:
            guess = input("\033[33m\nGuess a letter: \033[0m").lower()
            if is_valid_input(guess):
                break
            else:
                print("\033[31mInvalid input. Please enter a single letter (a-z or A-Z).\033[0m", end="")
        print("You guessed:", guess)  # for testing, later remove this line
        if guess not in secret_word:
            mistakes += 1
        else:
            guessed_letters.add(guess)
        if mistakes == MAX_NUMBER_OF_MISTAKES:
            display_game_state(mistakes, secret_word, guessed_letters, "lost")
            break
        elif set(secret_word) == guessed_letters:
            display_game_state(mistakes, secret_word, guessed_letters, "won")
            break
    if input("\033[33m\nEnter r to restart the game: \033[0m").lower() == "r":
        play_game()
    return None