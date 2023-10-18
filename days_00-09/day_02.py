print("Welcom to choose the treasure hunt!")
left_or_right = input("You come to a fork in the road. Do you want to go left or right? ")
if left_or_right == "right":
    print("Game over")
else:
    swim_or_wait = input("You come to a river. Will you swim or wait for a boat? ")
    if swim_or_wait == "swim":
        print("Game over")
    else:
        red_or_yellow_or_blue = input("Which door will you go through? red, yellow, or blue? ")
        if red_or_yellow_or_blue == "red" or red_or_yellow_or_blue == "yellow":
            print("Game over")
        else:
            print("You've found the treasure!")