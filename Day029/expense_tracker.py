
names = []
projects = []
payments = []
expenses = []


def client_names():
    name = input("Add client name: ")
    names.append(name)


def project_names():
    project = input("Add project name: ")
    projects.append(project)


def payment_amounts():
    payment = float(input("Add payment: "))
    payments.append(payment)


def business_expenses():
    expense = float(input("Add expense amount: "))
    expenses.append(expense)


def calculate_total_income():
    return sum(payments)


def calculate_total_expenses():
    return sum(expenses)


def calculate_net_profit():
    return calculate_total_income() - calculate_total_expenses()


def calculate_average_payment():
    if len(payments) == 0:
        return 0

    return calculate_total_income() / len(payments)


def highest_payment():
    if len(payments) == 0:
        return 0

    return max(payments)


def show_projects():
    if len(projects) == 0:
        print("No projects recorded.")
    else:
        for i in range(len(projects)):
            print(i + 1, projects[i])


def main():
    while True:
        print("\n===== FREELANCE TRACKER =====")
        print("1. Add client")
        print("2. Add project")
        print("3. Record payment")
        print("4. Record expense")
        print("5. View projects")
        print("6. Financial summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            client_names()

        elif choice == "2":
            project_names()

        elif choice == "3":
            payment_amounts()

        elif choice == "4":
            business_expenses()

        elif choice == "5":
            show_projects()

        elif choice == "6":
            print("\n===== FINANCIAL SUMMARY =====")
            print("Total Projects:", len(projects))
            print("Total Income:", calculate_total_income())
            print("Total Expenses:", calculate_total_expenses())
            print("Net Profit:", calculate_net_profit())
            print("Average Payment:", calculate_average_payment())
            print("Highest Payment:", highest_payment())

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()
