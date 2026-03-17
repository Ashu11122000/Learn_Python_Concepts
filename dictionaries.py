# Dictionary is a data structure that allows to store data in the form of key-value pair.
# It's syntax is: curly braces {}
# Dictionaries are ordered (in a particular, fixed sequence)
# Dictionaries are mutable (changeable)
# Dictionaries are duplicated (keys are unique, but values are duplicated)

# Importing JSON module: a built-in library in python that provides tools for converting Python objects into a JSON format.
import json

# Creating a dictionary
fruit_prices = {
    "apple": 0.99,
    "banana": 2.50,
    "blueberry": 3.00
}

print(fruit_prices)

# len() returns number of key-value pairs
print(len(fruit_prices))

# Adding new key-value pairs
fruit_prices["water melon"] = 4.00

# update() adds or modifies multiple values
fruit_prices.update({"cherry": 5.00})

print(fruit_prices)

# Removing key using pop()
fruit_prices.pop("apple")

print(fruit_prices)

# Checking if key exists using 'in'
if "kiwi" in fruit_prices:
    kiwi_price = fruit_prices["kiwi"]
    print(f"price of Kiwi is {kiwi_price}")
else:
    print("Kiwi not found!")

# Using get() to safely retrieve value
kiwi_price = fruit_prices.get("kiwi", 0)
print(f"price of Kiwi is {kiwi_price}")

# Looping through dictionary
for key in fruit_prices:
    print(key)
    print(fruit_prices[key])

# Nested Dictionary
shoe = {
    "name": "Nike AirMax 2020",
    "colors": ["red", "white", "black"],
    "price": 129.99,
}

print(shoe["name"])
print(shoe["price"])

# Convert Python dictionary to JSON string
result = json.dumps(shoe)

print(type(result))  # Output: <class 'str'>

# Dictionary Example: Tracking Expenses

# Creating a dictionary (key-value pairs)
# Keys are strings
# Values are integers
total_expenses = {
    "food": 40,
    "transport": 0,
    "shopping": 190
}

# Adding a new key-value pair
# If key does not exist, Python creates it
total_expenses["entertainment"] = 30

# Updating existing key using += operator
# Same as:
# total_expenses["food"] = total_expenses["food"] + 12
total_expenses["food"] += 12

# Printing the final dictionary
print(total_expenses)