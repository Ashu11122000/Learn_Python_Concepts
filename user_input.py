# User Input and File Writing Example

# input() takes user input as string
name = input("What is your name? ")
age = input("What is your age? ")

# Open file in write mode ("w")
# If file exists → it will overwrite
# If file does not exist → it will create it
with open("user_info.txt", "w") as f:

    # Write data into file using f-string
    # \n adds a new line
    f.write(f"{name} {age}\n")

# File automatically closes after this block