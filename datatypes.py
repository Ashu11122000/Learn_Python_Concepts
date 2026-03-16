# Example: Basic Python Data Types

# String (str)
# Stores text. Must be inside quotes.
item_name = "apple"

# Integer (int)
# Stores whole numbers (no decimals).
quantity = 4

# Float (float)
# Stores decimal numbers.
price_usd = 0.5

# Boolean (bool)
# Stores only True or False.
in_stock = True

# List: Ordered collection of items (can store multiple values)
fruits = ["apple", "banana", "cherry"]

#Tuple: Similar to list but immutable (cannot be changed).
dimensions = (10, 20, 30)

# Set: Unordered collection of unique values
numbers = {1, 2, 3, 4, 5}

# Dictionary: Stores data in key-value pairs
product= {
    "name": "apple",
    "price": 0.5,
    "quantity": 4
}

# Complex Numbers: Used for mathematical operations involving imaginary numbers
complex = 3 + 4j

# NoneType: Represents absence of value
discount = None

# Bytes: Stores binary data
byte_data = b"Python"

# ----------------------------------------
# print() function displays output.
# Each print statement prints one value.
# ----------------------------------------

print(type(item_name), item_name)   # Prints string
print(type(quantity), quantity)    # Prints integer
print(type(price_usd), price_usd)   # Prints float
print(type(in_stock), in_stock)    # Prints boolean

print(type(fruits), fruits)    # Prints list
print(type(dimensions), dimensions)    # Prints tuple
print(type(numbers), numbers)    # Prints set
print(type(product), product)    # Prints dictionary

print(type(complex), complex)    # Prints Complex numbers
print(type(discount), discount)    # Prints NoneType
print(type(byte_data), byte_data)    # Prints Bytes
