# Function Definition 
#1st function is printing which prints the string
def printing(str):
    print(str)
    return

# Now, call the function
printing("I'm first call to user-defined function!")
printing("Again second call to the same function!")


# This is a second function in which arguments passed as call by reference
def test(arg):
    print("Inside function:", arg)
    print("Id inside the function: ", id(arg))
    arg =arg.append(100)

var = [10, 20, 30, 40]
print("Id before passing: ", id(var))
test(var)
print("List after function call: ", var)

# This is a third function which prints hello {name} in which, I was passed arguments as values
def greetings(name):
    "This is a docstring of greetings function"

    # .format is used for String Formatting, which involves creating dynamic and well structured text by inserting variables and expressions into strings.
    print("Hello {}".format(name))
    return

greetings("Samay")
greetings("Pratima")
greetings("Steven")

# This is a 4th function which uses default arguments
def showinfo(name, city = "Hyderabad"):
    "This prints a passed info into this function"
    print("Name:", name)
    print("City:", city)
    return

showinfo(name = "Ansh", city = "Delhi")
showinfo(name = "Shrey")

# This is a 5th function which uses keyword arguments
#Function definition
def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age:", age)
    return
# Now I will call printinfo function by positional arguments
printinfo("Naveen", 29)
# Now, I will call printinfo function by keyword arguments
printinfo(name="miki", age = 30)

# 6th function uses Arbitrary arguments
# Sum of numbers
def add(*args):
    s = 0
    for x in args:
        s = s+x
    return s
result = add(29, 54, 67, 83)
print(result)

result = add(10, 20, 30, 40)
print(result)