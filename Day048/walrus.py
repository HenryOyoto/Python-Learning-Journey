import re

name = input("What is your name? ").strip()

# Using the Walrus operator ":="

if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(1) + " " + matches.group(2)

print(f"Hello {name}")