import sys
while True:
    try:
        age = int(input("Enter your age: "))
        print(f"Your age is {age} years")

        if age < 18:
            print("You are too young man, go play with toys ")
            sys.exit()
        break

    except ValueError:
        print("Enter your age in numbers/ symbols")
