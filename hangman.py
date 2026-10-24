import random

# List of words for the game
WORDS = [
    "PYTHON",
    "COMPUTER",
    "PROGRAM",
    "KEYBOARD",
    "DEVELOPER",
    "INTERNET",
    "HANGMAN"
]

# ASCII gallows stages: 0 to 6 incorrect guesses
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = set()
    max_attempts = 6

    print("=" * 35)
    print("       WELCOME TO HANGMAN!")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses allowed.")

    while True:
        # Display the gallows
        print(HANGMAN_STAGES[len(wrong_guesses)])

        # Display guessed and hidden letters
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("\nWord:", display_word)

        # Display previously guessed letters
        print(
            "Guessed letters:",
            " ".join(sorted(guessed_letters | wrong_guesses))
            or "None"
        )

        remaining = max_attempts - len(wrong_guesses)
        print(f"Attempts remaining: {remaining}")

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 35)
            print("CONGRATULATIONS! YOU WON!")
            print("The word was:", secret_word)
            print("=" * 35)
            break

        # Check for defeat
        if remaining == 0:
            print("\n" + "=" * 35)
            print("GAME OVER! YOU LOST!")
            print("The word was:", secret_word)
            print("=" * 35)
            break

        # Get and validate user input
        guess = input("\nEnter a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Please enter one English letter (A-Z).")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter. Try another!")
            continue

        # Record the guess
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            wrong_guesses.add(guess)
            print("Incorrect guess!")


if __name__ == "__main__":
    play_hangman()