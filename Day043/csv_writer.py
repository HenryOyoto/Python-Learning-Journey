import csv

name = input("What is your name? ")
school = input("Which school are you studying at? ")
house = input("Which house do you live in? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, school, house])