class Student:
    pass

def main():
    student = get_student()
    if student.name == "Jacob":
        student.house  = "Orion"
    print(f"{student.name} is from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()