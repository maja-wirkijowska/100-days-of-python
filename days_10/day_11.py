import random


def easy_difficulty(genned_num):
    check_guess(10, genned_num)


def hard_difficulty(genned_num):
    check_guess(5, genned_num)


def check_guess(lives, genned_num):
    while lives > 0:
        print(f"You have {lives} attempts remaining.")
        new_guess = int(input("Make a guess: "))
        if new_guess == genned_num:
            print(f"You win! The answer was {new_guess}!")
            lives = 0
        elif new_guess > genned_num:
            print("Too high!")
            lives -= 1
        elif new_guess < genned_num:
            print("Too low!")
            lives -= 1


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num_to_guess = random.randint(1, 100)

if difficulty == "easy":
    easy_difficulty(num_to_guess)
elif difficulty == "hard":
    hard_difficulty(num_to_guess)
else:
    print("That is not a valid difficulty.")

print("Good bye!")
