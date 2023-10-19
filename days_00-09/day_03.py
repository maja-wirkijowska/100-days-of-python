import random

player_selection = input("Select rock, paper, or scissors: ")
options = ["rock", "paper", "scissors"]
computer_selection = options[random.randint(0,2)]
print(f"Computer selected: {computer_selection}")
if player_selection == computer_selection:
    print("It's a DRAW")
elif player_selection == "rock" and computer_selection == "paper":
    print("You lose!")
elif player_selection == "rock" and computer_selection == "scissors":
    print("You win!")
elif player_selection == "paper" and computer_selection == "rock":
    print("You win!")
elif player_selection == "paper" and computer_selection == "scissors":
    print("You lose!")
elif player_selection == "scissors" and computer_selection == "paper":
    print("You win!")
elif player_selection == "scissors" and computer_selection == "rock":
    print("You lose!")
else:
    print("You didn't enter a valid option. You lose!")

