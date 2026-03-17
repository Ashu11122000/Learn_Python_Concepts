# This program decides whether I should make coffee right now.

# Boolean Variables
# A Boolean variable stores either True or False.
# Here, we are defining the current state of the cup and time of day.

is_cup_empty = False   # Boolean variable (False means the cup is NOT empty)
is_daytime = True      # Boolean variable (True means it is daytime)

# Logical Operator (AND)
# The 'and' operator returns True only if BOTH conditions are True.
# Syntax: condition1 and condition2
# If either condition is False, the result becomes False.
should_make_coffee = is_cup_empty and is_daytime

# Output using print()
# print() is a built-in Python function used to display output.
# It can print text (string) and variable values together.
print("Should I make coffee?", should_make_coffee)