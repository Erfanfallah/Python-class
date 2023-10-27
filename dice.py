import random

while True:
    op = input("roll or exit")
    if op == "exit":
        break
    if op == "roll":
        a=random.randint(1,6)
        print(a)
        if a==6:
            print("You can roll the dice again")
            a=random.randint(1,6)
            print(a)
            break