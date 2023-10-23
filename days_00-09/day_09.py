from os import system


def clear():
    _ = system('clear')


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


flag = True
result = 0.0
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_num = float(input("Enter a number: "))

while flag:

    for c in operations:
        print(c, end=" ")
    operation = input("\nSelect an operation: ")
    calc_function = operations[operation]
    second_num = float(input("Enter a number: "))

    result = calc_function(first_num, second_num)

    print(f"{first_num:.1f} {operation} {second_num:.1f} = {result:.1f}")

    keep_going = input("Type 'y' to continue with result, 'n' to start over, anything else to exit: ")
    if keep_going == "n" or keep_going == "N":
        clear()
        first_num = float(input("Enter a number: "))
    elif keep_going == "y" or keep_going == "Y":
        first_num = result
        print(f"First number: {first_num:.1f}")
    else:
        flag = False
        print("Good bye!")
