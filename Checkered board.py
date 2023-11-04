n = int(input("Enter n:"))
m = int(input("Enter m:"))
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print("*", end="")
    print()
