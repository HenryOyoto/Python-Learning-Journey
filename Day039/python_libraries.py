# Python Libraries
# import random
# def main():
#     coin = random.choice(["heads", "tails"])
#     print(coin)

# main()

# from random import choice
# def main():
#     coin = choice(["heads", "tails"])
#     print(coin)

# main()

# from random import randint
# def main():
#     number = randint(1, 10)
#     print(number)

# main()

# import random
# def main():
#     cards = ["John", "Henry", "Jerry", "Jacob"]
#     random.shuffle(cards)
#     for card in cards:
#         print(card)

# main()

from random import shuffle
def main():
    cards = ["John", "Henry", "Jerry", "Jacob"]
    shuffle(cards)
    for card in cards:
        print(card)

main()