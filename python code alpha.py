# create a simple text based hangman game where the player gussess a world one letter at a time
import random

# Predefined list of words
words = ["apple", "grape", "mango", "peach", "lemon"]

# Randomly choose a word
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
attempts_left = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word: " + " ".join(guessed_word))

# Game loop
while attempts_left > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        attempts_left -= 1
        print("Incorrect! Attempts left:", attempts_left)

    print("Current word: " + " ".join(guessed_word))

# Final outcome
if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("You lost! The word was:", word_to_guess)
