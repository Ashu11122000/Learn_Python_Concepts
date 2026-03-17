# List is a Data Structure that allows to store and work with a lot of data at once.
# The syntax of Lists: square braces []
# Lists are ordered (defined and fiexed sequence)
# Lists are mutable (changeable)
# Lists are duplicated (a list contains multiple identical elements, or a full list has been copied to another.)

# Creating an empty list
fruit_basket = []

# Printing empty list
print("Initial Empty List:", fruit_basket)

# len() returns number of elements in the basket
print("\n Length:", len(fruit_basket))

# Adding elements in fruit_basket list
# append() add items to the end of the list
fruit_basket.append("banana")
fruit_basket.append("apple")
fruit_basket.append("carrot")

# \n is used for new line
print("\n After adding elements: ", fruit_basket)
print("\n Length:", len(fruit_basket))

# insert() add item at specific index
fruit_basket.insert(1, "mango")    # Insert at index 1
print("\n After Insert:", fruit_basket)

# extend() adds multiple elements at once
fruit_basket.extend(["grapes", "orange"])
print("\n After extend:", fruit_basket)

# Removing Elements
# remove() removes item by value
fruit_basket.remove("carrot")
print("\n After remove carrot:", fruit_basket)

# pop() removes item by index
removed_item = fruit_basket.pop(2)
print("\n Popped Item:", removed_item)
print("\n After pop:", fruit_basket)

# del also removes item by index
del fruit_basket[0]
print("\n After del index 0:", fruit_basket)
print("\n Length:", len(fruit_basket))

# Accessing Elements
# Accessing element using index (0 = first element)
print("\n First element:", fruit_basket[0])

# Negative indexing (last element)
print("\n Last element:", fruit_basket[-1])

# List Slicing
# Syntax: list[start:end]
# Includes start index, excludes end index
list = [2, 4, 6, 0, 1, 3, 5]
slice_list = list[0:3]

print("\n Original list:", list)
print("Sliced list (0:3): ", slice_list)

# Reverse Slicing
print("\n Reversed slicing:", list[::-1])

# Sorting and Reversing
numbers = [5, 2, 9, 1, 7]

# sort() modifies original list
numbers.sort()
print("\n Sorted List:", numbers)

# reverse() reverses list
numbers.reverse()
print("\n Reversed List:", numbers)

# sorted() returns new sorted list (does not change original)
new_sorted = sorted(numbers)
print("\n New Sorted List:", new_sorted)

# Splitting (String -> List)
# split() converts string into list
sentence = "apple banana mango orange"
words = sentence.split(" ")    # split by space
print("\n Split words:", words)

# Joining (List -> String)
# join() coverts list into string
joined_sentence = " - ".join(words)
print("\n Joined sentence:", joined_sentence)

# 2D Lists
# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n 2D List (Matrix):")
print(matrix)

# Accessing elements in 2D list
print("\n Element at row 1, col 2:", matrix[1][2])

# Looping through 2D list
print("\n Iterating through matrix:")
for row in matrix:
    for item in row:
        print(item, end = " ")
    print()    # new line after each row

# List Comprehension
# Creating list using comprehension
squares = [x**2 for x in range(5)]
print("\n Squares:", squares)

# Filtering using comprehension
# List comprehension is a short and powerful way to create lists in Python in a single line, istead of using long loops.
even_numbers = [x for x in range(10) if x % 2 == 0]
print("\n Even numbers: ", even_numbers)