from tkinter import *
import random
from tkinter import messagebox
import copy
import math

#create a root window

root = Tk()
canvas = Canvas(root, width=506, height=506, bg = "#4F4F4F")

""""""""""""""""""""""""""""""""""""""""""""""""""

#config window size and color and title and whatever
root.title("Conway's Game of Life (reconstructed by Mark Anthony)")
root.geometry("510x510")
root.config(bg="white")

#defining variables

Alv = 1
Ded = 0

#defining functions

def click_handler(event):
    if event.num == 1 and row[event.y] == Ded and column[event.x] == Ded:
        Cell(event.x, event.y) 

def Cell(x, y):
    r = math.floor((x+5)/10)
    x = r*10
    z = math.floor((y+5)/10)
    y = z*10
    canvas.create_line(x-5, y-1, x+4, y-1, width = 9, fill='yellow')
    

#making a lot of lines and shit

for i in range(51):
    canvas.create_line(4, 4+(i*10), 505, 4+(i*10), width = 1)
    canvas.create_line(4+(i*10), 4, 4+(i*10), 505, width = 1)
    
canvas.create_line(4, 4, 4, 505)
canvas.create_line(4, 4, 505, 4)

canvas.pack()

column = []
row = []
for i in range(50):
    row.append(0)
for i in range(50):
    grid.append(copy.deepcopy(row))

root.bind("<Button>", click_handler)

#keeping the interface up
root.mainloop()
