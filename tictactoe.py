import tkinter as tk


def draw_cross(event):

    global draw_cross_next

    x = event.x
    y = event.y
    print(x,y)
    print()
    #now get the correct cell
    x1 = x//300 * 300   #left upper corner of given cell
    y1 = y//300 * 300   #left upper corner of given cell
    print(x1, y1)
    print()
    x2 = x1+300
    y2 = y1+300

    x11 = x1+300
    x22 = x2-300
    if draw_cross_next:
        canvas.create_line(x1, y1, x2, y2, fill = "black")
        canvas.create_line(x11, y1, x22, y2, fill = "black")
    else:
        canvas.create_oval(x1, y1, x2, y2)

    draw_cross_next = not draw_cross_next

   # print(x1, y1, x2, y2)




root = tk.Tk()
root.geometry("900x900")

canvas = tk.Canvas(root, width=900, height=900)
canvas.pack()

canvas.create_line(300, 0, 300, 900, fill="black") #(x1, y1), (x2, y2)
canvas.create_line(600, 0, 600, 900, fill="black")

canvas.create_line(0, 300, 900, 300, fill="black")
canvas.create_line(0, 600, 900, 600, fill="black")


draw_cross_next = True

canvas.bind("<Button-1>", draw_cross)


root.mainloop()



