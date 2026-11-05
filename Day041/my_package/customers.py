
customers = []


def add_customer(name, email):
    customer = {
        "name": name,
        "email": email
    }

    customers.append(customer)
    return f"Customer {name} added successfully."


def find_customer(email):
    for customer in customers:
        if customer["email"] == email:
            return customer

    return "Customer not found."


def display_customers():
    if not customers:
        return "No customers registered."

    for customer in customers:
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print("-" * 30)
