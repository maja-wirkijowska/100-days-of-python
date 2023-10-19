print("welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
num_people_splitting_bill = int(input("How many people are splitting the bill? "))
tip_percentage = int(input("What tip percentage would you like to give? 10, 12, or 15? ")) / 100
bill_portion = (total_bill + (total_bill * tip_percentage)) / num_people_splitting_bill
print(f"Each person should pay ${bill_portion:.2f}")
