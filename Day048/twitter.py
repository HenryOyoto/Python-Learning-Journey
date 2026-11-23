import re

url = input("Enter your Twitter URL ").strip()

username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Your Username is {username}")
