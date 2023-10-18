import random

lives = 6
word_list = ["polymorphism", "inheritance", "abstraction", "encapsulation"]
chosen_word = word_list[random.randint(0,3)]

display = []
for letter in chosen_word:
    display += "_"
print(f"{display}\n")

used_letters = [] 
flag = True

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess == "end":
        break
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives = lives -1
    print(f"{display}")
    print(f"Lives: {lives}")
    if guess not in used_letters:
        used_letters.append(guess)
    print(f"Used letters: {used_letters}\n")
    
if "_" in display:
    print("YOU'RE A LOSER!!\n")
else:
    print("YOU WIN!!\n") 
