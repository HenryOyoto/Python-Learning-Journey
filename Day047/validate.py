""" Regular expressions library"""
import re

while True:
    email = input("What's your email address? ").strip()
    if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|org|net)$", email, re.IGNORECASE):
        print("Valid")
        print(f"Your email is {email.lower()}")
        break
    else:
        print("Invalid")
    

