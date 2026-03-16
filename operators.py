# An Expression is a combination of values, variables, operators, and anything else that basically results in a single value once you compute it.
# An Evaluation in Python is the process of interpreting an expression and determining its value.

x = 100  # "=" is used as Assignment operator
y = 52   # "=" is used as Assignment operator
z = 40   # "=" is used as Assignment operator

# ---------------- ASSIGNMENT OPERATORS ----------------
x += 20   # Add and assign
y -= 2    # Subtract and assign
z *= 2    # Multiply and assign

print("Updated values after assignment operators:")
print("x =", x)
print("y =", y)
print("z =", z)

# ---------------- ARITHMETIC OPERATORS ----------------
print("\nArithmetic Operators")
print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x / y)   # Division
print(x // y)  # Floor Division
print(x % y)   # Modulus
print(x ** 2)  # Exponentiation
print(x + y * z)  # Order of precedence

# ---------------- COMPARISON OPERATORS ----------------
print("\nComparison Operators")
print(x == y)  # Equals
print(x != y)  # Not Equals
print(x < y)   # Less than
print(x > y)   # Greater than
print(x <= y)  # Less than or equal to
print(x >= y)  # Greater than or equal to

# ---------------- LOGICAL OPERATORS ----------------
print("\nLogical Operators")
print(x and y)  # AND operator
print(x or y)   # OR operator
print(not x)    # NOT operator

# ---------------- BITWISE OPERATORS ----------------
print("\nBitwise Operators")
print(x & y)   # AND
print(x | y)   # OR
print(x ^ y)   # XOR
print(~x)      # NOT
print(x << 2)  # Left shift
print(x >> 2)  # Right shift

# ---------------- MEMBERSHIP OPERATORS ----------------
print("\nMembership Operators")
numbers = [10, 20, 30, 40, 50]

print(20 in numbers)       # True if value exists
print(100 in numbers)      # False
print(30 not in numbers)   # False
print(70 not in numbers)   # True

# ---------------- IDENTITY OPERATORS ----------------
print("\nIdentity Operators")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (same object in memory)
print(a is c)     # False (different objects)
print(a is not c) # True