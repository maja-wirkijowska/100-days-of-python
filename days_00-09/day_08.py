from os import system
import operator


def clear():
    _ = system('clear')


def find_max_bid(name_bid):
    max_value = max(name_bid.items(), key=operator.itemgetter(1))[0]
    return max_value


print("Welcome to the Secret Auction Program!")
keep_going = ""
name_bid_dict = {}
flag = True
while flag:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    if name not in name_bid_dict:
        name_bid_dict[name] = bid
    else:
        name_bid_dict.update({name: bid})

    while keep_going != "y" or keep_going != "n":
        keep_going = input("Are there any other bidders? [y/n]")
        if keep_going == "n":
            flag = False
            max_bid = find_max_bid(name_bid_dict)
            print(f"The winner is {max_bid} with a bid of ${name_bid_dict[max_bid]}")
            break
        elif keep_going == "y":
            clear()
            break
