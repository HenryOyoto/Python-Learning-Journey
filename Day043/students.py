# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, school = line.rstrip().split(",")
#         student = {"name": name, "school": school}
#         students.append(student)


# def get_name(student):
#     return student["name"]


# for student in sorted(students, key=get_name, reverse=True): # DONT'T PARENTHESIS for get_name
#     print(f"{student['name']} is in {student['school']}")

##USING lambda
students = []
with open("students.csv") as file:
    for line in file:
        name, school = line.rstrip().split(",")
        student = {"name": name, "school": school}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['school']}")