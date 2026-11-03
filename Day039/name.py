from sys import argv
from sys import exit

def main():
    try:
        if len(argv) > 2:
            exit("Too Many Arguments")

        print("Hello, my name is ", argv[1])

    except IndexError:
        print("Too few arguments ")

    

main()