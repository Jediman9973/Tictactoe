def winner(board):
    """checking rows"""
    for i in board:
        if all(x == 'X' for x in i):         #i is sublist in board and I iterate through it with x
            return 1

    for i in board:
        if all(x == 'O' for x in i):
            return -1


    """checking columns"""
    for i in range(0, 3):
        if all(sublist[i] == 'X' for sublist in board):               #I check first element of each sublist, then second of each and finally third of each
            return 1

    for i in range(0, 3):
        if all(sublist[i] == 'O' for sublist in board):               #I check first element of each sublist, then second of each and finally third of each
            return -1


    """checking diagonals"""
    if all(board[i][i] == 'X' for i in range(3)):
        return 1

    if all(board[i][i] == 'O' for i in range(3)):
        return -1

    if all(board[i][2-i] == 'X' for i in range(3)):
        return 1

    if all(board[i][2-i] == 'O' for i in range(3)):
        return -1

    return 0




def minimax(board, player):
    score_curr = winner(board)

    if score_curr != 0:
        return score_curr

    if not any("" in row for row in board):
        return 0

    if player == "X":           #it was called with X, so X just played and now O is going to play
        best_score = 2
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, "O")
                    best_score = min(score, best_score)
                    board[i][j] = ""
        return best_score


    if player == "O":
        best_score = -2
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, "X")
                    best_score = max(score, best_score)
                    board[i][j] = ""
        return best_score




def bestmove_for_X(board):
    move = None
    bestscore = -2
    #find an empty cell
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                score = minimax(board, "X")
                board[i][j] = ""
                if score > bestscore:
                    move = (i, j)
                    bestscore = score
    return move

def bestmove_for_O(board):
    move = None
    bestscore = 2
    #find an empty cell

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, "O")
                board[i][j] = ""
                if score < bestscore:
                    move = (i, j)
                    bestscore = score
    return move


board = [
    ["O", "O", "X"],
    ["X", "X", ""],
    ["O", "O", ""]
]
