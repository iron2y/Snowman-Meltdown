import random
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
        print(f"Game Over! The word was: {secret_word}")
        return None
    elif state == "won":
        print(f"Congratulations, you saved the snowman!\nYou guessed the word: {secret_word}")
        return None
    hidden_word = create_word_hint(secret_word, guessed_letters)
    print(f"Word: {hidden_word}")
    return None


def is_valid_input(guess):
    """Checks if the input is a valid letter."""
    return len(guess) == 1 and guess.isalpha()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = set()
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        while True:
            guess = input("\nGuess a letter: ").lower()
            if is_valid_input(guess):
                break
            else:
                print("Invalid input. Please enter a single letter (a-z or A-Z).", end="")
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