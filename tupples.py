# Tuple: Data structure in python
# Syntac of tuple: round braces ()
# Tuples are immutable (not changeable)
# Tuples data should be duplicated
# Tuples are ordered (in a particular, fixed manner/sequence)
# We can accessing data/item using index.
# We can't add or remove data item from tuple.
# Actually using tuple as a keys within dictionary.

# Tuple Example

# Creating a tuple (immutable sequence)
my_tuple = ("apple", "kiwi", "banana")

# Tuple unpacking
# Assigns values to variables in order
x, y, z = my_tuple

print(x, y, z)

# Using Tuple as Dictionary Key

# Create empty dictionary
board = {}

# Tuples are immutable → can be used as keys
board[(1, 1)] = True

# Another tuple representing position
position = (3, 4)

# Check if key exists in dictionary
if position in board:
    print(board[position])
else:
    print(False)