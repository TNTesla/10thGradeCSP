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
root.geometry("510x540")
root.config(bg="#3C3C3C")

#defining variables

Alv = 1
Ded = 0

#defining functions

def click_handler(event):
    if event.num == 1 and grid[math.floor((event.x-5)/10)][math.floor((event.y-5)/10)] == Ded:
        Cell(event.x, event.y)
    else:
        Uncell(event.x, event.y)

def Cell(x, y):
    r = math.floor((x+5)/10)
    x = r*10
    z = math.floor((y+5)/10)
    y = z*10
    canvas.create_line(x-5, y-1, x+4, y-1, width = 9, fill='yellow')
    grid[math.floor((x-5)/10)][math.floor((y-5)/10)] = Alv
    
def Uncell(x, y):
    r = math.floor((x+5)/10)
    x = r*10
    z = math.floor((y+5)/10)
    y = z*10
    canvas.create_line(x-5, y-1, x+4, y-1, width = 9, fill='#4F4F4F')
    grid[math.floor((x-5)/10)][math.floor((y-5)/10)] = Ded

#

    #The big boy; generation difference coding.

def gigaSuperHell():
        #the loops to check each block
    for a in range(50):
        for b in range(50):
            
            #the loops to scan if alive cells stay alive
            if grid[a][b] == Alv:
                    if grid[a-1][b-1] ==Alv:
                        pass



#making a lot of lines and shit

for i in range(51):
    canvas.create_line(4, 4+(i*10), 505, 4+(i*10), width = 1)
    canvas.create_line(4+(i*10), 4, 4+(i*10), 505, width = 1)
    
canvas.create_line(4, 4, 4, 505)
canvas.create_line(4, 4, 505, 4)

grid = []
row = []
for i in range(50):
    row.append(0)
for i in range(50):
    grid.append(copy.deepcopy(row))

canvas.pack()

root.bind("<Button>", click_handler)

#keeping the interface up
root.mainloop()
