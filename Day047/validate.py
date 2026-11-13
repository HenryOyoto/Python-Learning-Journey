""" Regular expressions library"""
import re

email = input("What's your email address? ")

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")

else:
    print("Invalid")
