import random

def create_new_password(total_capital, total_little, total_symbols, total_nums):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_chars = "!@# $%^&*<>?~:;"
    genned_password = []
    for i in range(0, total_capital):
        j = random.randint(0, len(uppercase_letters) - 1)
        genned_password.append(uppercase_letters[j])   
    
    for i in range(0, total_little):
        j = random.randint(0, len(lowercase_letters) - 1)
        genned_password.append(lowercase_letters[j]) 
    
    for i in range(0, total_symbols):
        j = random.randint(0, len(special_chars) - 1)
        genned_password.append(special_chars[j])     

    for i in range(0, total_nums):
        j = random.randint(0, len(numbers) - 1)
        genned_password.append(numbers[j]) 
      
    return genned_password

print("Welcome to the password generator!")
num_total_chars = int(input("How many total characters do you need in your password? "))
num_uppercase_letters = int(input("How many upercase letters do you need in your password? "))
num_special_chars = int(input("How many special characters do you need in your password? "))
num_numbers = int(input("How many numbers do you need in your password? "))
num_lowercase_letters = num_total_chars - (num_uppercase_letters + num_special_chars + num_numbers)
print(f"The remaining {num_lowercase_letters} characters will be lowercase letters.")
new_password = create_new_password(num_uppercase_letters, num_lowercase_letters, num_special_chars, num_numbers)
random.shuffle(new_password)
new_password = "".join(new_password)
print(f"Your password is: {new_password}")
