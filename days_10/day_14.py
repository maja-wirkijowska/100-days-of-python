MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100},
        "cost": 3.0
    }
}
resources = {"water": 300, "coffee": 200, "milk": 100}
coins = {"quarters": 8, "dimes": 10, "nickels": 20, "pennies": 25}
profit = 0


def count_coins(change_needed):
    """Counts the amount of each coin needed"""
    q = int(change_needed // 0.25)
    change_needed = round(change_needed % 0.25, 2)
    d = int(change_needed // 0.10)
    change_needed = round(change_needed % 0.10, 2)
    n = int(change_needed // 0.05)
    change_needed = round(change_needed % 0.05, 2)
    p = int(change_needed // 0.01)
    return q, d, n, p


def enough_coins_to_make_change(available_coins, change_needed):
    """Returns True if enough coins available to make change"""
    list_coins = list(count_coins(change_needed))
    needed = {"quarters": list_coins[0], "dimes": list_coins[1], "nickels": list_coins[2], "pennies": list_coins[3]}
    for coin in needed:
        if needed[coin] > available_coins[coin]:
            print(f"Not enough of {coin} coins to process transaction.")
            return False
    return True


def is_resource_sufficient(needed_ingredients):
    """Returns True if there are sufficient ingredients, False if not"""
    for item in needed_ingredients:
        if needed_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True


def process_paid_coins():
    """Returns the amount paid in coins"""
    print("Insert coins")
    total = int(input("Number of quarters: ")) * 0.25
    total += int(input("Number of dimes: ")) * 0.10
    total += int(input("Number of nickels: ")) * 0.05
    total += int(input("Number of pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True is money paid is enough, False if not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if enough_coins_to_make_change(coins, change):
            print(f"Here is ${change} in change.")
            global profit
            profit += drink_cost
            return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit:.2f}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_paid_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])




