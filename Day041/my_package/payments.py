
def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")

    return price * quantity


def apply_discount(total, discount):
    if total < 0:
        raise ValueError("Total cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    discount_amount = total * (discount / 100)

    return total - discount_amount


def generate_receipt(customer_name, total):
    return (
        f"\nPAYMENT RECEIPT\n"
        f"Customer: {customer_name}\n"
        f"Amount paid: KSh {total:.2f}\n"
        f"Thank you for shopping with us!"
    )
