import random


def main():
    cards = ["jack", "queen", "king"]
    random.seed(0)  # Helps in debugging
    print(random.choices(cards, weights=[60, 30, 10], k=2))
    print(random.sample(cards, k=2))


main()
