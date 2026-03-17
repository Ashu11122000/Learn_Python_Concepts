# Set: useful data structure in Python
# Sets are not ordered (order of storing data/element/item in set doesn't matter)
# Syntax of Sets: In curly braces {} as well as in round braces ()
# Sets are mutable (changeable)
# There is no duplication of data in sets.

# Set Operations Example

# Creating a set of favorite fruits
favorite_fruits = {"apple", "banana", "cherry", "blackberry", "water melon"}

# Adding element to set
favorite_fruits.add("kiwi")

# Removing element from set
favorite_fruits.remove("kiwi")

# Another set of red fruits
red_fruits = {"apple", "strawberry", "cherry", "water melon"}

# Find common elements (intersection)
favorite_red_fruits = favorite_fruits.intersection(red_fruits)

# Find all unique elements (union)
favorite_red_fruits = favorite_fruits.union(red_fruits)

# Print results
print(favorite_fruits)
print(favorite_red_fruits)