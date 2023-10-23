import math

op = input("enter op(+, /, *, -, sin, cos, tan, cot, factorial, sqrt):")

if op == "cos":
    x = float(input("Enter x:"))
    r = (math.cos(math.radians(x)))

if op == "cot":
    x = float(input("Enter x:"))
    z = (math.tan(math.radians(x)))
    r = 1 / z

if op == "sin":
    x = float(input("Enter x:"))
    r = (math.sin(math.radians(x)))

if op == "sqrt":
    x = float(input("Enter x:"))
    r = (math.sqrt(x))

if op == "tan":
    x = float(input("Enter x:"))
    r = (math.tan(math.radians(x)))

if op == "factorial":
    x = int(input("Enter x:"))
    r = (math.factorial(x))

if op == "/":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    if b == 0:
        r = "Error"
    else:
        r = a / b

if op == "*":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a * b

if op == "+":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a + b

if op == "-":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a - b

print(r)
