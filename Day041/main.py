
from my_package import customers, inventory, payments


def main():
    # Register customers
    print(customers.add_customer("Henry", "henry@email.com"))
    print(customers.add_customer("James", "james@email.com"))

    # Add products
    print(inventory.add_product("Laptop", 65000, 5))
    print(inventory.add_product("Mouse", 1200, 20))

    # Display records
    print("\nCUSTOMER RECORDS")
    customers.display_customers()

    print("\nINVENTORY RECORDS")
    inventory.display_inventory()

    # Process a payment
    price = 65000
    quantity = 1

    total = payments.calculate_total(price, quantity)
    discounted_total = payments.apply_discount(total, 10)

    receipt = payments.generate_receipt(
        "Henry",
        discounted_total
    )

    print(receipt)


if __name__ == "__main__":
    main()
