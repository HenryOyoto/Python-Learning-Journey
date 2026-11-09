# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello, ", line.rstrip())

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello, ", line, end="")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello, ", line.strip())

names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")

# with open("names.txt") as file:
#     for line in sorted(file):
#         print(f"Hello, {line.rstrip()}")

## To sort in descending order from Z to A

with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}")