import re

def main():
    code = input("Enter Hexadecimal colour code ")

    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")

    else:
        print("Invalid")

main()