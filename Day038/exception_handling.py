# Handling exceptions
# Raising exceptions

def main():
    print("======== STUDENT REGISTRATION SYSTEM ========")
    register_student()

def register_student():
    try:
        # Accept student information
        name = input("Enter student name: ")
         # RAISED ERROR: Name must contain letters only
        if not name.replace(" ", "").isalpha():
            raise ValueError("Student name must contain letters only.")
        
        age = int(input("Enter your age: "))
        marks = float(input("Enter exam marks: "))
        units = int(input("Enter number of units: "))

        # RAISED ERROR 1
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        # RAISED ERROR 2
        if age < 16:
            raise ValueError("Student must be at least 16 years old.")

        # RAISED ERROR 3
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        # RAISED ERROR 4
        if units < 1 or units > 10:
            raise ValueError("Units must be between 1 and 10.")


        print("\nRegistration successful!")
        print("Name:", name)
        print("Age:", age)
        print("Marks:", marks)
        print("Units:", units)

    # EXCEPTION 1
    except ValueError as e:
        print("Input Error:", e)

    # EXCEPTION 2
    except KeyboardInterrupt:
        print("\nRegistration cancelled.")

    # EXCEPTION 3
    except Exception as e:
        print("Unexpected Error:", e)

main()