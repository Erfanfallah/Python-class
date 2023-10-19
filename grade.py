name = input("Please enter your name:")

family = input("Please enter your Family name:")

a = int(input("Please enter the grade of the first lesson:"))

b = int(input("Please enter the grade of the second lesson:"))

c = int(input("Please enter the grade of the third lesson:"))

average = ((a + b + c) / 3)

if average >= 17:
    print("Dear", name, family, "your result is Great")

if 17 > average >= 12:
    print("Dear", name, family, "your result is Normal")

if average < 12:
    print("Dear", name, family, "Your result is fail. Please try harder")
