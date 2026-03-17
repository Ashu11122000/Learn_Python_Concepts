# Local Variable Scope
def localFunction():
    a = 10
    b = 20
    print("Variable a:", a)
    print("Variable b:", b)
    return a+b
print(localFunction())

# Global Variable Scope
#global variables
name = 'Ashish'
marks = 70
def globalFunction():
   # accessing inside the function
   print("name:", name)
   print("marks:", marks)
# function call   
globalFunction()

# Non-Local Variable Scope
def nonLocalFunction():
    a = 5
    b = 6
    # nested function
    def nestedFunction():
        # nonlocal function
        nonlocal a
        nonlocal b
        a = 10
        b = 20
        print("Variable a:", a)
        print("Variable b:", b)
        return a+b
    
    print(nestedFunction())

nonLocalFunction()