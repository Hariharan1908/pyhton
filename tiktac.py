def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    for row in board:
        if any(cell == " " for cell in row):
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            turn += 1
        else:
            print("That spot is already taken. Try again.")

tic_tac_toe()
