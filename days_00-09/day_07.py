def encrypt(send, num):
    alphanumeric = list("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    encoded = []
    shifted_letters_nums = shift(num)
    for letter in send:
        index = alphanumeric.index(letter)
        encoded.append(shifted_letters_nums[index])
    return encoded

def decrypt(receive, num):
    alphanumeric = list("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    decoded = []
    shifted_letters_nums = shift(num)
    for letter in receive:
        index = shifted_letters_nums.index(letter)
        decoded.append(alphanumeric[index])
    return decoded

def shift(shift_amount):
    alphanumeric = list("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shifted_letters_nums = []
    end = alphanumeric[:shift_amount]
    front = alphanumeric[shift_amount:]
    shifted_letters_nums = front + end
    return shifted_letters_nums


print("Caesar Cypher")
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
        encoded_message = encrypt(message, shift_num)
        encoded_message = "".join(encoded_message)
        print(f"Your encoded message is: {encoded_message}")
    elif option == "d":
        decoded_message = decrypt(message, shift_num)
        decoded_message = "".join(decoded_message)
        print(f"You decoded message is: {decoded_message}")
                
    loop = input("Type \'y\' to continue or \'n\' to stop: ")
    if loop == "n":
        print("Good bye!")
        keep_going = False
    