import tkinter as tk
from minimax_mine import winner, bestmove_for_O

def computer_move():
    global board, draw_cross_next
    move = bestmove_for_O(board)
    if move is not None:
        board[move[0]][move[1]] = 'O'
        draw_o(move)
        draw_cross_next = True  # Allow the player to make the next move


def draw_o(move):
    x1, y1 = move[1] * 300, move[0] * 300
    x2, y2 = x1 + 300, y1 + 300
    canvas.create_oval(x1, y1, x2, y2)

def draw_cross(event):
    global draw_cross_next

    #if not draw_cross_next:
        #return  # Skip if it's not the player's turn

    x, y = event.x, event.y
    x1, y1 = (x // 300) * 300, (y // 300) * 300
    x2, y2 = x1 + 300, y1 + 300
    cell_X, cell_Y = x // 300, y // 300

    if board[cell_Y][cell_X] == "":
        canvas.create_line(x1, y1, x2, y2, fill="black")
        canvas.create_line(x1 + 300, y1, x2 - 300, y2, fill="black")
        board[cell_Y][cell_X] = "X"
        draw_cross_next = False

        if not winner(board):
            computer_move()  # Computer's move


    if winner(board):
        print("You lost!")                  #We don't have to check who won, because we can't win against ideal player anyway

    if not any("" in row for row in board):
        print("Tie!")


root = tk.Tk()
root.geometry("900x900")

canvas = tk.Canvas(root, width=900, height=900)
canvas.pack()

# Creating the board
canvas.create_line(300, 0, 300, 900, fill="black") #(x1, y1), (x2, y2)
canvas.create_line(600, 0, 600, 900, fill="black")
canvas.create_line(0, 300, 900, 300, fill="black")
canvas.create_line(0, 600, 900, 600, fill="black")

# Board for internal state
board = [
    ["", "", ""],  # Row 0
    ["", "", ""],  # Row 1
    ["", "", ""]   # Row 2
]

draw_cross_next = True
canvas.bind("<Button-1>", draw_cross)
root.mainloop()
