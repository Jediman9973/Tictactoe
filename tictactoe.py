import tkinter as tk

def winner():
    """checking rows"""
    for i in board:
        if (all(x == 'X' for x in i) or all(x == 'O' for x in i)):        #i is sublist in board and I iterate through it with x
            return True

    """checking columns"""
    for i in range(0, 3):
        if (all(sublist[i] == 'X' for sublist in board)) or (all(sublist[i] == 'O' for sublist in board)):               #I check first element of each sublist, then second of each and finally third of each
            return True

    """checking diagonals"""
    if(all(board[i][i] == 'X' for i in range(3))) or ((all(board[i][i] == 'O' for i in range(3)))):
        return True

    if (all(board[i][2-i] == 'X' for i in range(3))) or (all(board[i][2-i] == 'O' for i in range(3))):
        return True

    return False

def draw_cross(event):

    global draw_cross_next

    x = event.x
    y = event.y

    #now get the correct cell
    x1 = x//300 * 300   #left upper corner of given cell
    y1 = y//300 * 300   #left upper corner of given cell

    x2 = x1+300
    y2 = y1+300

    x11 = x1+300        #for second line
    x22 = x2-300

    cell_X = x//300
    cell_Y = y//300

    if board[cell_Y][cell_X] == "":
        if draw_cross_next:
            canvas.create_line(x1, y1, x2, y2, fill = "black")
            canvas.create_line(x11, y1, x22, y2, fill = "black")

            board[cell_Y][cell_X] = "X"             #writing to internal state

        else:
            canvas.create_oval(x1, y1, x2, y2)
            board[cell_Y][cell_X] = "O"             #writing to internal state

    if winner():
        print("oujé")


    draw_cross_next = not draw_cross_next


root = tk.Tk()
root.geometry("900x900")

canvas = tk.Canvas(root, width=900, height=900)
canvas.pack()

#creating the board
canvas.create_line(300, 0, 300, 900, fill="black") #(x1, y1), (x2, y2)
canvas.create_line(600, 0, 600, 900, fill="black")

canvas.create_line(0, 300, 900, 300, fill="black")
canvas.create_line(0, 600, 900, 600, fill="black")


#board for internal state
board = [
    ["", "", ""],  # Row 0
    ["", "", ""],  # Row 1
    ["", "", ""]   # Row 2
]

draw_cross_next = True
win = 0

canvas.bind("<Button-1>", draw_cross)


root.mainloop()



