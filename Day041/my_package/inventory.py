
products = []


def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    return f"{name} added to inventory."


def check_stock(name):
    for product in products:
        if product["name"].lower() == name.lower():
            return product["quantity"]

    return "Product not found."


def display_inventory():
    if not products:
        return "Inventory is empty."

    for product in products:
        print(f"Product: {product['name']}")
        print(f"Price: KSh {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print("-" * 30)
