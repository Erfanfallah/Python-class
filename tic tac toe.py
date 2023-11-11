def show():
    for row in game_bord:
        for cell in row:
            print(cell, end=" ")
        print()


def check_game():
    # player1
    if game_bord[0][0] == "o" and game_bord[0][1] == "o" and game_bord[0][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[1][0] == "o" and game_bord[1][1] == "o" and game_bord[1][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[2][0] == "o" and game_bord[2][1] == "o" and game_bord[2][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[0][0] == "o" and game_bord[1][0] == "o" and game_bord[2][0] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[0][1] == "o" and game_bord[1][1] == "o" and game_bord[1][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[0][2] == "o" and game_bord[1][2] == "o" and game_bord[2][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[0][0] == "o" and game_bord[1][1] == "o" and game_bord[2][2] == "o":
        print("Player1 Win!")
        return 1
    if game_bord[2][0] == "o" and game_bord[1][1] == "o" and game_bord[0][2] == "o":
        print("Player1 Win!")
        return 1
    # ---------------------------------------------------------------------------------
    # player2
    # ---------------------------------------------------------------------------------
    if game_bord[0][0] == "x" and game_bord[0][1] == "x" and game_bord[0][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[1][0] == "x" and game_bord[1][1] == "x" and game_bord[1][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[2][0] == "x" and game_bord[2][1] == "x" and game_bord[2][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[0][0] == "x" and game_bord[1][0] == "x" and game_bord[2][0] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[0][1] == "x" and game_bord[1][1] == "x" and game_bord[1][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[0][2] == "x" and game_bord[1][2] == "x" and game_bord[2][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[0][0] == "x" and game_bord[1][1] == "x" and game_bord[2][2] == "x":
        print("Player2 Win!")
        return 1
    if game_bord[2][0] == "x" and game_bord[1][1] == "x" and game_bord[0][2] == "x":
        print("Player2 Win!")
        return 1


game_bord = [["-", "-", "-"],
             ["-", "-", "-"],
             ["-", "-", "-"]]

# player 1 => o
while True:
    print("player 1")
    while True:
        row = int(input("Enter row:"))
        col = int(input("Enter col"))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_bord[row][col] == "-":
                game_bord[row][col] = "o"
                show()
                break
            else:
                print("yek khoneh digeh entkhab kon!!!")
        else:
            print("yek khoneh digeh entkhab kon!!!")
    if check_game() == 1:
        break

    if game_bord[0][0] != "-" and game_bord[0][1] != "-" and game_bord[0][2] != "-" and game_bord[1][0] != "-" and \
            game_bord[1][1] != "-" and game_bord[1][2] != "-" and game_bord[2][0] != "-" and game_bord[2][
        1] != "-" and game_bord[2][2] != "-" and check_game() != 1:
        print("The game equalised!")
        break

    # player 2
    print("player 2")
    while True:
        row = int(input("Enter row:"))
        col = int(input("Enter col"))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_bord[row][col] == "-":
                game_bord[row][col] = "x"
                show()
                break
            else:
                print("yek khoneh digeh entkhab kon!!!")
        else:
            print("yek khoneh digeh entkhab kon!!!")
    if check_game() == 1:
        break

    if game_bord[0][0] != "-" and game_bord[0][1] != "-" and game_bord[0][2] != "-" and game_bord[1][0] != "-" and \
            game_bord[1][1] != "-" and game_bord[1][2] != "-" and game_bord[2][0] != "-" and game_bord[2][
        1] != "-" and game_bord[2][2] != "-" and check_game() != 1:
        print("The game equalised!")
        break
