import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    number_of_trials = 3
    while True:
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word:
            print("snowman_full")
        else:
            print("snwoman_reduced")
            number_of_trials -= 1
            if number_of_trials == 0:
                print(f"Game Over! The word was: {secret_word}")
                break


if __name__ == "__main__":
    play_game()