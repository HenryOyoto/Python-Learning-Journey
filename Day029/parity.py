def main():
    x = int(input("Enter the value of X: "))

    if is_even(x):
        print("X is an even number! ")

    elif is_odd(x):
        print("X is an odd number! ")

    else:
        print("I don't understand You! ")

def is_even(x):
    return x % 2 == 0 

def is_odd(x):
    return x % 2 != 0 

main()
    


