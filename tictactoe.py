board = ["-","-","-","-","-","-","-","-","-"]
winner = None

def gameplay():
    global winner
    print("Welcome Tic Tac Toe in your face!!!")
    showBoard()

    for p1 in range(5):
        print("Player one's turn - X")
        value = "X"
        move(value)
        isWinner()
        if winner != "X" and p1 < 4:
            for p2 in range(3):
                print("Player two's turn - O")
                value = "O"
                move(value)
                isWinner()
                if winner == "O":
                    print("Player two wins! Congrats!!!")
                break
        elif winner == "X":
            print("Player one wins! Congrats!!!")
            break
        else:
            print("It's a tie! Better luck next time!!!")

# check winner
def isWinner():
    global winner
    # horinzontal check
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
    # vertical check
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
    # diagonal check
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]

# choose position and make a move
def move(value):
    make_move = False

    while make_move == False:
        position = int(input("Choose a position between 1 and 9: "))
        position -= 1

        if board[position] == "-":
            make_move = True
        else:
            print("This position is already filled")

    board[position] = value
    showBoard()

# show the board
def showBoard():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}           1 | 2 | 3")
    print(f"{board[3]} | {board[4]} | {board[5]}           4 | 5 | 6")
    print(f"{board[6]} | {board[7]} | {board[8]}           7 | 8 | 9")
    print("\n")

gameplay()