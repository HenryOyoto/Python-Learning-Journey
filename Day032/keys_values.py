# .keys(): This is a dictionary method that returns all the dictionary keys.
# .values(): This is a dictionary method that returns all the dictionary values

def main():
    details = {
        "Henry": "25",
        "Jerry": "24",
        "Abraham": "23",
        "Kelvin": "26",
        "Jovan": "27"
    }

    for name in details.keys():
        print(f"The age of {name} is {details[name]}")

    print("\n\n")

    for age in details.values():
        print(f"The age of {name} is {age}")

main()
