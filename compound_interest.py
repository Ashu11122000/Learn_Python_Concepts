# Compound Interest Calculation

# Integer with underscore for readability
# Python ignores the underscore
principal = 240_000    # Initial amount of money (int)

# Float data type (decimal number)
annual_rate = 0.05     # 5% interest rate (float)

years = 2              # Number of years (int)

# Arithmetic Operators Used:
# +  -> Addition
# *  -> Multiplication
# ** -> Exponent (power)
#
# Formula: A = P(1 + r)^t
# Python follows order of operations (PEMDAS - Parentheses, Exponents, Multiplication & Division (left to right), and Addition & Subtraction (left to right))
amount = principal * (1 + annual_rate) ** years

# print() displays output
print("Total amount after", years, "years:", amount)