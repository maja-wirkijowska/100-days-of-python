def binary_search(input_list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(input_list) - 1
    if high < low:
        return -1

    midpoint = (low + high) // 2
    if input_list[midpoint] == target:
        return midpoint
    elif target < input_list[midpoint]:
        return binary_search(input_list, target, low, midpoint - 1)
    else:
        return binary_search(input_list, target, midpoint + 1, high)


list_len = int(input("Enter the number of elements you want in the list: "))
num_list = []
i = 0
while i < list_len:
    temp = int(input("Enter a number: "))
    num_list.append(temp)
    i += 1

num_list.sort()
target_num = int(input("Enter target number: "))
found_index = binary_search(num_list, target_num)
if found_index == -1:
    print(f"This list doesn't contain {target_num}")
else:
    print(f"Number {target_num} is at index number {found_index}")
