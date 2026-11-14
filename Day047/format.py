import re
name = input("What is your name? ").strip()

matches = re.search(r"^(.+), (.+)", name)
if matches:
    last, first = matches.groups()
    name = f"{last} {first}"

print(f"Hello, {name}")


