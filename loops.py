# FOR LOOP with enumerate()
# A list containing some fruits
fruit_basket = ["apple", "banana", "blueberry"]

# enumerate() returns both the index and the value of each item in the list
for i, fruit in enumerate(fruit_basket):
    # f-string allows inserting variables directly inside a string
    print(f"There is a {fruit} in the basket at index {i}")
    
    # Simple print statement
    print("This is yummy!")

# FOR LOOP with range()
# range(start, stop) generates numbers from start to stop-1
# Here it will generate numbers from 1 to 99
for i in range(1, 100):
    print(f"Looping {i} times")

# WHILE LOOP with continue and break
# Initialize counter variable
count = 0

# Infinite loop (runs forever until break statement stops it)
while True:
    count += 1   # Increment count by 1 each iteration

    # continue skips the rest of the loop for this iteration
    if count == 3:
        continue

    # Print current count value
    print(f"This has run {count} times!")

    # break stops the loop completely
    if count == 5:
        break

# Code continues here after loop ends
print("Welcome back!")

# LIST COMPREHENSION
# Original list of numbers
my_list = [2, 4, 6, 0, 1, 3, 5]

# Print original list
print(my_list)

# List comprehension:
# Creates a new list where each element of my_list is multiplied by 2
new_list = [2 * x for x in my_list]

# Print new transformed list
print(new_list)

# SIMPLE FOR LOOP OVER A LIST
# A list containing words
words = ["one", "two", "three"]

# Iterate through each element of the list
for x in words:
    print(x)

# FOR LOOP WITH TUPLE + SUM + EVEN CHECK
# A tuple containing numbers
numbers = (34, 54, 67, 21, 78, 97, 45, 44, 80, 19)

# Variable to store sum of numbers
total = 0

# Iterate through each number in the tuple
for num in numbers:
    total += num  # Add current number to total

    # Check if number is even
    if num % 2 == 0:
        print(num)  # Print even numbers only

# Print total sum
print("Total:", total)

# FOR LOOP WITH RANGE + ELSE
# Loop from 0 to 5
for count in range(6):
    # format() inserts value inside string
    print("Iteration no. {}".format(count))

# The else block runs after the for loop completes normally
else:
    print("for loop over. Now in else block")
print("End of for loop")

# WHILE LOOP
# Initialize counter
count = 0

# Loop runs while condition is True
while count < 5:
    count += 1
    print("Iteration no. {}".format(count))

# Executed after while loop ends
print("End of while loop")