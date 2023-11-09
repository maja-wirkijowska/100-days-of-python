print("LIST COMPREHENSION")
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(f"1. {squared_numbers}")

list_of_strings = ["1", "1", "2", "3", "5", "8", "13", "21", "34", "55"]
list_of_ints = [int(i) for i in list_of_strings]
print(f"2. {list_of_ints}")

with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()
result = [int(num) for num in list1 if num in list2]
print(f"3. {result}")

print("\nDICTIONARY COMPREHENSION")
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split(" ")
sentence_dict = {word: len(word) for word in sentence}
print(f"1. {sentence_dict}")

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14,
             "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {(day, temp * 9 / 5 + 32) for (day, temp) in weather_c.items()}
print(f"2. {weather_f}")

