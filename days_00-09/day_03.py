import random

player_selection = input("Select rock, paper, or scisors: ")
options = ["rock", "paper", "scisors"]
computer_selection = options[random.randint(0,2)]
print(f"Computer selected: {computer_selection}")
if player_selection == computer_selection:
    print("It's a DRAW")
elif player_selection == "rock" and computer_selection == "paper":
    print("You lose!")
elif player_selection == "rock" and computer_selection == "scisors":
    print("You win!")
elif player_selection == "paper" and computer_selection == "rock":
    print("You win!")
elif player_selection == "paper" and computer_selection == "scisors":
    print("You lose!")
elif player_selection == "scisors" and computer_selection == "paper":
    print("You win!")
elif player_selection == "scisors" and computer_selection == "rock":
    print("You lose!")
else:
    print("You didn't enter a valid option. You lose!")

