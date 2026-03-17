# Nested Loop Pattern Example

# Outer loop runs 5 times (0 to 4)
for i in range(5):

    # Reset message string each time outer loop runs
    message = ""

    # Inner loop runs i+1 times
    # range(i+1) means:
    # when i=0 → 1 time
    # when i=1 → 2 times
    # when i=2 → 3 times
    for sub_number in range(i + 1):

        # += appends value to string
        # f-string converts number to string automatically
        message += f"{sub_number}"

    # Print constructed string after inner loop finishes
    print(message)