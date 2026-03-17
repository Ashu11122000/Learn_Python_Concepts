# Entry Pricing Decision System

# Integer variable (stores age)
customer_age = 24

# Boolean variable (stores student status)
is_student = False

# Conditional Statements (Control Flow)
# Python evaluates conditions top to bottom

# Check if customer is under 18
if customer_age < 18:
    print("Entry is Free")

# Check if customer is student OR senior citizen
# 'or' returns True if at least one condition is True
elif is_student or customer_age > 65:
    print("Entry is at 50% off")

# If none of the above conditions are True
else:
    print("Entry is at full price")