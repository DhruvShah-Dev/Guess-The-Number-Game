import random

def guess_the_number():
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    while True:
        try:
            # Get user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
