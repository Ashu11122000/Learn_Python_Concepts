# break Statement
x = 0

while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")


# continue Statement
for letter in "Python":
    # continue when letter is 'h'
    if letter == "h":
        continue
    print("Current Letter:", letter)

# if-else condition statement
var = 98
if var == 100:
    print("The number is equalt to 100")

elif var > 0:
    print("The given number is positive")
    if var % 2 == 0:
        print("The given number is even")
    else:
        print("The given number is odd")

elif var == 0:
    print("The given number is zero")

else:
    print("The given number is negative")