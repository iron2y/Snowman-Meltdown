import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

MAX_NUMBER_OF_MISTAKES = 3


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def create_word_hint(secret_word, found_letters):
    """Creates a word hint based on the secret word."""
    if found_letters:
        hidden_word = ""
        for char in secret_word:
            if char in found_letters:
                hidden_word += char
            else:
                hidden_word += "_"
    else:
        hidden_word = "_" * len(secret_word)
    return " ".join(hidden_word)


def display_game_state(mistakes, secret_word, found_letters, state=""):
    """Displays the current game state."""
    print(STAGES[mistakes])
    if state == "lost":
        print(f"Game Over! The word was: {secret_word}")
        return None
    elif state == "won":
        print(f"Congratulations, you saved the snowman!\nYou guessed the word: {secret_word}")
        return None
    hidden_word = create_word_hint(secret_word, found_letters)
    print(f"Word: {hidden_word}")
    return None


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = set()
    found_letters = set()
    while True:
        display_game_state(mistakes, secret_word, found_letters)
        guess = input("\nGuess a letter: ").lower()
        guessed_letters.add(guess)
        print("You guessed:", guess)  # for testing, later remove this line
        if guess not in secret_word:
            mistakes += 1
        else:
            found_letters.add(guess)
        if mistakes == MAX_NUMBER_OF_MISTAKES:
            display_game_state(mistakes, secret_word, found_letters, "lost")
            break
        elif set(secret_word) == found_letters:
        #elif set(secret_word) == found_letters:
            display_game_state(mistakes, secret_word, found_letters, "won")
            break


if __name__ == "__main__":
    play_game()