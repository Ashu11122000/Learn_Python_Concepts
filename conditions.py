# Transportation Decision Program

# Boolean variable (stores True or False)
is_raining = False

# Integer variable
distance_km = 12

# Conditional Statements
# Python checks conditions from top to bottom.
if is_raining:
    # Runs if it is raining
    print("Drive to Destination!")

elif distance_km > 10:
    # Runs if it is NOT raining AND distance is greater than 10
    print("Cycle to Destination!")

else:
    # Runs if none of the above conditions are True
    print("Walk to Destination!")