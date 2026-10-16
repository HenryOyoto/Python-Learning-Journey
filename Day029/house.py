name = input("Enter your name: ")

match name:
    case "Henry" | "John" | "Jacob":
        print("Pennynsula")
    case "Jerry":
        print("KK Towers")
    case "Abraham":
        print("Sula Towers")
    case _:
        print("Who is that")

    