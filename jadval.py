while True:
    op = input("To use the program, type Continue or type exit:")

    if op == "exit":
        break
    else:
        print("Choose a number between 1 and 10 or exit")
        m = int(input("Enter row:"))
        n = int(input("Enter col:"))

        if m > 11 or n > 11 or m < 1 or n < 1:
            print("error")
            print("You entered a wrong numberChoose a number between 1 and 10")
            print("Choose a number between 1 and 10 or exit")
            m = int(input("Enter row:"))
            n = int(input("Enter col:"))

        multiplication_table = [["x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                [1, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [2, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [3, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [4, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [5, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [6, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [7, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [8, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [9, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [10, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                                [11, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], ]

        for i in range(m):
            for j in range(n):
                multiplication_table[i + 1][j + 1] = (multiplication_table[i + 1][0]) * (multiplication_table[0][j + 1])

        for i in range(m):
            for j in range(n):
                print(multiplication_table[i][j], end=" ")
            print()
