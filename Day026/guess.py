def get_guess():
    guess = input("Enter a Guess: ")
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect! Try again.")

main()