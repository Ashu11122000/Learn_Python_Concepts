# Packing
def packFunction(*args):
    print("Packed arguments:", args)
packFunction(1, 2, 3, 'a', 'b')

# Unpacking
def unpackingFunction(a, b, c):
    print("Unpacked arguments:", a, b, c)
values = [1, 2, 3]
unpackingFunction(*values)

# tuples
tup = (10, 20, 30, 40, 50, 60)
x, *y, z = tup
print("x:", x, "y:", y, "z:", z)

# Packing Arguments
def packArguments(*args):
    print("Packed arguments:", args)
# Calling the function with multiple arguments
packArguments(1, 2, 3, 'a', 'b')

# ** operator is used to unpack a dictionary into individual keyword arguments
# **kwargs (Keyword Arguments) in Python allows a function to accept an arbitary number of Keyword Arguments, which are collected from dictionary.
def unpackKwargs(name, age, city):
    print("Unpacked Keyword arguments:", name, age, city)
# Dictionary of values to unpack
info = {"name": "Farhan", "age": 25, "city": "Los Angeles"}
#calling the function with unpacked values
unpackKwargs(**info)

# Real world example of packing and unpacking
# Function that accepts variable number of items (packing with *args)
def calculate_total(*items):
    print("Items in cart:", items)
    return sum(items)

# Function that accpets variable keyword arguments (packing with **kwargs)
def printInvoice(customer_name, **details):
    print(f"Invoice for {customer_name}")
    for key, value in details.items():
        print(f"{key}:{value}")

# Unpacking
# Order Items (list of prices)
order_items = [250, 100, 75]    # Prices of products
total_amount = calculate_total(*order_items)    # Unpacking list
print("Total Amount:", total_amount)

# Order Details (dictionary)
order_details = {
    "Product": "Laptop",
    "Quanity": 1,
    "Price": total_amount,
    "Paymeny Method": "Credit Card"
}

# Passing dictionary as Keyword args
printInvoice("Farhan", **order_details)