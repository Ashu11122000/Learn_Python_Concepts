# A Class is a blueprint or template used to create objects. 
# It defines properties (variables) and behaviors (methods/functions).
# Example: Product class defines name, calories, and price.

# An object is an instance of a class.
# It represents a real-world entity with actual values.
# Example: banana, tomato, potato are objects of Product class.

# f"string" is used to insert variables or expressions directly inside a string.
# We use {} to include variables.
# Example: f"My name is {name}"
# It makes code cleaner and more readable.

# Class Definition
class Product:
    
    # __init__ is a constructor method
    # It runs automatically when an object is created
    # It initializes object attributes (variables)
    def __init__(self, name, calories, price_per_kg):
        self.name = name              # Assign name to object
        self.calories = calories      # Assign calories value
        self.price_per_kg = price_per_kg  # Assign price per kg

    # Method to print product name using f-string
    def do_something(self):
        # f-string inserts self.name inside the string
        print(f"This is a {self.name}")
    
    # Method to calculate total price based on weight
    def get_price(self, weights_kgs):
        # Multiply price per kg with weight
        return self.price_per_kg * weights_kgs
        
# Creating Objects
banana = Product("banana", 105, 10.0)   # Creating object banana
tomato = Product("tomato", 22, 2.1)     # Creating object tomato
potato = Product("potato", 162, 0.9)    # Creating object potato

# Access Object Properties
# Print attributes of banana object
print(banana.name, banana.calories, banana.price_per_kg)

# Print attributes of tomato object
print(tomato.name, tomato.calories, tomato.price_per_kg)

# Print attributes of potato object
print(potato.name, potato.calories, potato.price_per_kg)

# Calling method that uses f-string
banana.do_something()

# Calling method to calculate price for 4 kg
print(banana.get_price(4.0))