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
