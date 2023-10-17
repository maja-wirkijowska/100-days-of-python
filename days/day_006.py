def letter_to_number(c):
    if c in "ABC":
        return "2"
    elif c in "DEF":
        return "3"
    elif c in "GHI":
        return "4"
    elif c in "JKL":
        return "5"
    elif c in "MNO":
        return "6"
    elif c in "PQRS":
        return "7"
    elif c in "TUV":
        return "8"
    elif c in "WXYZ":
        return "9"

def parenthesis_format(phone_num):
    return "(" + phone_num[0] + ") " + phone_num[1] + "-" + phone_num[2]

def periods_format(phone_num):
    seperator = "."
    return seperator.join(phone_num)
    
phone_num = input("Enter a 10-digit phone number without punctuation: ")
while not phone_num.isalnum():
    phone_num = input("Make sure to enter a number without punctuation: ")
    
while len(phone_num) != 10:
    phone_num = input("Be sure to enter a 10-digit phone number: ")
    
phone_num = phone_num.upper()
for c in phone_num:
    if c.isupper():
        phone_num = phone_num.replace(c, letter_to_number(c))

phone_num = [phone_num[0:3], phone_num[3:6], phone_num[6:]]
print(parenthesis_format(phone_num))
print(periods_format(phone_num))
