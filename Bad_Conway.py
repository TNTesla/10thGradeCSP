from tkinter import *
import random
from tkinter import messagebox
import copy

#create a root window

root = Tk()
canvas = Canvas(root, width=506, height=506, bg = "#4F4F4F")

""""""""""""""""""""""""""""""""""""""""""""""""""

#config window size and color and title and whatever
root.title("Conway's Game of Life (reconstructed by Mark Anthony)")
root.geometry("510x510")
root.config(bg="white")

#defining variables

infLo = 0

#defining functions

def click_handler(event):
    if event.num == 2:
        Cell(event.x, event.y) 

def Cell(x, y):
    canvas.create_line(x, y, x+8, y, width = 5, fill='yellow')
    

def togCel(x, y):
    pass

#making a lot of lines and shit

for i in range(51):
    canvas.create_line(4, 4+(i*10), 505, 4+(i*10), width = 1)
    canvas.create_line(4+(i*10), 4, 4+(i*10), 505, width = 1)
    
canvas.create_line(4, 4, 4, 505)
canvas.create_line(4, 4, 505, 4)

canvas.pack()

grid = []
row = []
for i in range(25):
    row.append(0)
for i in range(25):
    grid.append(copy.deepcopy(row))

root.bind("<Button>", click_handler)

#keeping the interface up
root.mainloop()
