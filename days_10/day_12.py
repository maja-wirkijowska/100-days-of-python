def fizz_buzz(user_num):
    answer = ""
    if user_num % 3 == 0 and user_num % 5 == 0:
        answer = "FizzBuzz"
    elif user_num % 3 == 0:
        answer = "Fizz"
    elif user_num % 5 == 0:
        answer = "Buzz"
    return answer


number = int(input("Enter an integer: "))
for i in range(1, number + 1):
    answer_string = fizz_buzz(i)
    if answer_string == "":
        print(i)
    else:
        print(answer_string)
