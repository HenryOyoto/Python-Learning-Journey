"""This is trial code"""

import csv

name = input("What are your three names? ").strip()
firstname, middlename, surname = name.split(" ")

fullname = firstname + middlename + surname
name = fullname

csv.write("Number1.csv")
name = csv.save("Number1.csv")