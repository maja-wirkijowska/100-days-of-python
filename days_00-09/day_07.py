def encrypt(letters_nums, send, num):
    encoded = []
    shifted_letters_nums = shift(letters_nums, num)
    for letter in send:
        index = letters_nums.index(letter)
        encoded.append(shifted_letters_nums[index])
    return encoded

def decrypt(letters_nums, receive, num):
    decoded = []
    shifted_letters_nums = shift(letters_nums, num)
    for letter in receive:
        index = shifted_letters_nums.index(letter)
        decoded.append(letters_nums[index])
    return decoded

def shift(letters_nums, shift_amount):
    shifted_letters_nums = []
    end = letters_nums[:shift_amount]
    front = letters_nums[shift_amount:]
    shifted_letters_nums = front + end
    return shifted_letters_nums


print("Caesar Cypher")
alphanumeric = list("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
keep_going = True
while keep_going:
    option = input("Type \'e\' to encrypt and \'d\' to decrypt: ")  
    if option != "e" and option != "d":
        keep_going = False
        print("That is not a valid selection. Good bye!")  
        break
    
    message = input("Type your message: ")
    shift_num = int(input("Enter a shift amount: "))
    
    if option == "e":
        encoded_message = encrypt(alphanumeric, message, shift_num)
        encoded_message = "".join(encoded_message)
        print(f"Your encoded message is: {encoded_message}")
    elif option == "d":
        decoded_message = decrypt(alphanumeric, message, shift_num)
        decoded_message = "".join(decoded_message)
        print(f"You decoded message is: {decoded_message}")
                
    loop = input("Type \'y\' to continue or \'n\' to stop: ")
    if loop == "n":
        print("Good bye!")
        keep_going = False
    