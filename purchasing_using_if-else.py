# Original amount before discount
amount = 2500

# Print the initial amount
print('Amount = ', amount)

# Check if amount is greater than 10000
# If true, customer gets 20% discount
if amount > 10000:
    discount = amount * 20 / 100

# If the above condition is false, check next condition
else:
    # If amount is greater than 5000, apply 10% discount
    if amount > 5000:
        discount = amount * 10 / 100

    # If amount is not greater than 5000, check next condition
    else:
        # If amount is greater than 1000, apply 5% discount
        if amount > 1000:
            discount = amount * 5 / 100

        # If none of the above conditions match, no discount
        else:
            discount = 0
    
# Print the final payable amount after subtracting discount
print('Payable amount =', amount - discount)