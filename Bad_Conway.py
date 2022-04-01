from tkinter import *
import random
from tkinter import messagebox
import copy
import math

#create a root window

root = Tk()

#dumb useless button to make things less dumb
butn = Button(root, text = ".")
butn.place(x = 400, y = 0)

#canvas so i can make this less stupid overall

canvas = Canvas(root, width=506, height=506, bg = "#4F4F4F")

""""""""""""""""""""""""""""""""""""""""""""""""""

#config window size and color and title and whatever
root.title("Conway's Game of Life (reconstructed by Mark Anthony)")
root.geometry("1020x1080")
root.config(bg="#3C3C3C")

#defining variables

Alv = 1
Ded = 0


#defining functions

def click_handler(event):
    if event.y < 506:
        if event.num == 1 and grid[math.floor((event.x-5)/10)][math.floor((event.y-5)/10)] == Ded:
            Cell(event.x, event.y)
        else:
            Uncell(event.x, event.y)
    else:
        pass

def Cell(x, y):
    r = math.floor((x+5)/10)
    p = r*10
    z = math.floor((y+5)/10)
    c = z*10
    canvas.create_line(p-5, c-1, p+4, c-1, width = 9, fill='yellow')
    grid[math.floor((x-5)/10)][math.floor((y-5)/10)] = Alv
    print("cell")
    
def Uncell(x, y):
    r = math.floor((x+5)/10)
    p = r*10
    z = math.floor((y+5)/10)
    c = z*10
    canvas.create_line(p-5, c-1, p+4, c-1, width = 9, fill='#4F4F4F')
    grid[math.floor((x-5)/10)][math.floor((y-5)/10)] = Ded
    print("uncell")


#The big boy; generation coding.

def gigaSuperHell():
    
    #the loops to check each block
    for a in range(50):
        for b in range(50):
            alvNeigh = 0
            #the loops to scan 'neighbors'
            if grid[a][b] == Alv:
                    if grid[a-1][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a-1][b] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b] ==Alv:
                        alvNeigh += 1
                    if grid[a-1][b+1] ==Alv:
                        alvNeigh += 1
                    if grid[a][b+1] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b+1] ==Alv:
                        alvNeigh += 1
                    #killing/spawning cells
                    if alvNeigh <= 1:
                        grid[a][b] = Ded
                        canvas.create_line((a+1)*10-5, (b+1)*10-1, (a+1)*10+4, (b+1)*10-1, width = 9, fill='#4F4F4F')
                    elif alvNeigh >= 4:
                        grid[a][b] = Ded
                        canvas.create_line((a+1)*10-5, (b+1)*10-1, (a+1)*10+4, (b+1)*10-1, width = 9, fill='#4F4F4F')
                    else:
                        grid[a][b] = Alv
                        canvas.create_line((a+1)*10-5, (b+1)*10-1, (a+1)*10+4, (b+1)*10-1, width = 9, fill='yellow')
                    
                    alvNeigh = 0
            
            if grid[a][b] == Ded:
                    if grid[a-1][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b-1] ==Alv:
                        alvNeigh += 1
                    if grid[a-1][b] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b] ==Alv:
                        alvNeigh += 1
                    if grid[a-1][b+1] ==Alv:
                        alvNeigh += 1
                    if grid[a][b+1] ==Alv:
                        alvNeigh += 1
                    if grid[a+1][b+1] ==Alv:
                        alvNeigh += 1
                    
                    #killing/spawning cells
                    if alvNeigh == 3:
                        grid[a][b] = Alv
                        canvas.create_line((a+1)*10-5, (b+1)*10-1, (a+1)*10+4, (b+1)*10-1, width = 9, fill='yellow')
                    
                    alvNeigh = 0




#Making the button for the god forsaken generation code

btn = Button(root, text = "                                                Run one Generation                                                ", font = ("Arial", 12), bg = "#4F4F4F", fg = "black", command = gigaSuperHell)
btn.place(x = 400, y = 510)

#making a lot of lines and shit

for i in range(51):
    canvas.create_line(4, 4+(i*10), 505, 4+(i*10), width = 1)
    canvas.create_line(4+(i*10), 4, 4+(i*10), 505, width = 1)
    
canvas.create_line(4, 4, 4, 505)
canvas.create_line(4, 4, 505, 4)

grid = []
row = []
for i in range(51):
    row.append(Ded)
for i in range(51):
    grid.append(copy.deepcopy(row))

canvas.pack()

root.bind("<Button>", click_handler)

#keeping the interface up
root.mainloop()
