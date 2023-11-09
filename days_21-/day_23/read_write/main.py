with open("read_write_file.txt", mode="w") as file:
    file.write("new line")

with open("read_write_file.txt", mode="a") as file:
    file.write(f"\nanother line")

with open("read_write_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
