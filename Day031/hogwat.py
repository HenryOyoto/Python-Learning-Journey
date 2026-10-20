# A new keyword called None in python which shows that item has no value

students = [
    {"name": "Henry", "house": "Pennynsula", "food": "Chicken"},
    {"name": "Jerry", "house": "Springvale", "food": "Meat"},
    {"name": "Jovan", "house": "Losandas", "food": "Dairy"},
    {"name": "Abraham", "house": "Pennsilvania", "food": None}
]

for student in students:
    print(student["name"], student["house"], sep=":  ")

