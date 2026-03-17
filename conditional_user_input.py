x = int(input("Enter your age:"))
y = input("Are you a citizen of India (yes/no)?: ")

if x >= 18:
    if y.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Must be a citizen to vote.")
else:
    print("Must be atleast 18 years old to vote.")