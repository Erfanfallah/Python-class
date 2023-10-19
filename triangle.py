print("To create a triangle you need to enter its three sides")

a = int(input("Please enter the first side:"))

b = int(input("Please enter the second side:"))

c = int(input("Please enter the third side:"))

if a < b + c:
    if b < a + c:
        if c < a + b:
            print("The sides you entered can form a triangle")
else:
    print("Unfortunately, the sides you entered cannot form a triangle. try again")
