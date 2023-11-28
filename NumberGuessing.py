import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set up a loop to continue guessing until the player guesses the correct number
while True:
    # Get the player's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is too high or too low
    if guess > secret_number:
        print("Your guess is too high.")
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        # The player guessed correctly!
        print("Congratulations🎉! You guessed the correct number.")
        print(" ")
        break

print("Game over.")
