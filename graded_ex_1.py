# graded_ex_1.py

# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    """Returns a list of products sorted by the specified order. Anything other than 'desc' is considered ascending."""
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))



def display_products(products_list):
    """Displays the products in a numbered format."""
    for i, (product, price) in enumerate(products_list, 1):
        print(f"{i}. {product} - ${price}")


def display_categories():
    """Displays the available product categories and returns the user's choice index."""
    print("Available Categories:")
    for i, category in enumerate(products, 1):
        print(f"{i}. {category}")

    for _ in range(3):  # Maximum 3 attempts
        try:
            choice = int(input("Select a category by number: "))
            if 1 <= choice <= len(products):
                return choice - 1
            print(f"Invalid choice. Please select a number between 1 and {len(products)}.")
        except (ValueError, EOFError, StopIteration):
            print("Invalid input or no more input available.")
            return None
    print("Too many invalid attempts. Exiting.")
    return None



def add_to_cart(cart, product, quantity):
    """Adds the selected product and quantity to the cart."""
    cart.append((product[0], product[1], quantity))  # Add (Product Name, Price, Quantity) to the cart


def display_cart(cart):
    """Displays the cart contents and calculates the total cost."""
    total_cost = 0
    for item in cart:
        name, price, quantity = item
        cost = price * quantity
        print(f"{name} - ${price} x {quantity} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")
    return total_cost  # Return total cost for further use


def generate_receipt(name, email, cart, total_cost, address):
    """Generates and displays a receipt for the customer."""
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        print(f"{item[2]} x {item[0]} - ${item[1]} = ${item[1] * item[2]}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    """Validates that the name contains only two parts and only alphabets."""
    parts = name.strip().split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    """Validates that the email contains an '@' symbol."""
    return "@" in email and email.count("@") == 1 and email.find("@") > 0 and email.find("@") < len(email) - 1


def get_user_name():
    """Prompts the user for their name and validates it."""
    for _ in range(3):
        try:
            name = input("Enter your full name (first and last): ")
            if validate_name(name):
                return name
            print("Invalid name. Please enter again.")
        except EOFError:
            print("No more input available.")
            return None
    print("Too many invalid attempts.")
    return None



def get_user_email():
    """Prompts the user for their email and validates it."""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            email = input("Enter your email: ")
            if validate_email(email):
                return email
            else:
                print("Invalid email. Please enter again.")
        except (EOFError, StopIteration):
            print("No more input available.")
            return None
        attempts += 1
    print("Too many invalid attempts.")
    return None


def select_product(product_list):
    """Prompts the user to select a product and returns the selected product."""
    prompt = f"Select a product by number (1-{len(product_list)}): "
    for _ in range(3):
        try:
            product_choice = int(input(prompt))
            if 1 <= product_choice <= len(product_list):
                return product_list[product_choice - 1]
            print(f"Invalid choice. Please select a number between 1 and {len(product_list)}.")
        except (ValueError, EOFError):
            print("Invalid input or no more input available.")
            return None
    print("Too many invalid attempts. Exiting.")
    return None


def get_quantity(product_name):
    """Prompts the user for the quantity and validates the input."""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            quantity_input = input(f"How many {product_name}s would you like to buy? ")
            if not quantity_input:
                print("No input detected.")
                return None
            quantity = int(quantity_input)
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")
        except (EOFError, StopIteration):
            print("No more input available.")
            return None
        attempts += 1
    print("Too many invalid attempts.")
    return None


def get_address():
    """Prompts the user for their delivery address and validates the input."""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        try:
            address = input("Enter your delivery address: ")
            if address.strip():
                return address
            else:
                print("Address cannot be empty.")
        except (EOFError, StopIteration):
            print("No more input available.")
            return None
        attempts += 1
    print("Too many invalid attempts.")
    return None


def main():
    cart = []

    # Welcome message
    print("Welcome to the Online Store!")
    print("You can browse products by category, add them to your cart, and proceed to checkout.")
    print("Let's get started!\n")

    # Step 1: Ask for user's name and validate it
    name = get_user_name()
    if name is None:
        print("No valid name provided. Exiting program.")
        return

    # Step 2: Ask for user's email and validate it
    email = get_user_email()
    if email is None:
        print("No valid email provided. Exiting program.")
        return

    while True:
        # Step 3: Display categories and ask user to select one
        category_choice = display_categories()
        if category_choice is None:
            print("No valid category selected. Exiting program.")
            return
        category = list(products.keys())[category_choice]

        # Step 4: Display products in the selected category
        product_list = products[category]

        # Ask if the user wants to sort the products
        sort_order = input("Would you like to sort the products by price? Enter 'asc' for ascending, 'desc' for descending, or press Enter to skip: ").lower()
        if sort_order in ['asc', 'desc']:
            product_list = display_sorted_products(product_list, sort_order)

        display_products(product_list)

        # Step 5: Ask user to select a product
        selected_product = select_product(product_list)
        if selected_product is None:
            print("No valid product selected. Exiting program.")
            return

        # Step 6: Ask for quantity and add to cart
        quantity = get_quantity(selected_product[0])
        if quantity is None:
            print("No valid quantity provided. Exiting program.")
            return
        add_to_cart(cart, selected_product, quantity)

        # Ask if the user wants to continue shopping
        continue_shopping = input("Would you like to continue shopping? (yes/no): ").lower()
        if continue_shopping != 'yes':
            break

    # Step 7: Display cart
    total_cost = display_cart(cart)

    # Step 8: Get delivery address
    address = get_address()
    if address is None:
        print("No valid address provided. Exiting program.")
        return

    # Step 9: Generate receipt
    generate_receipt(name, email, cart, total_cost, address)


# Run the program
if __name__ == "__main__":
    main()
