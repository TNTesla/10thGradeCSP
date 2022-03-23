from tkinter import *
import random
from tkinter import messagebox

#create a root window

root = Tk()
canvas = Canvas(root, width=500, height=500, bg = "#4F4F4F")

"""""""""""""""""""""""""""""""""""""""""""""""""""
"""           """"""           """"""           """
"""           """"""           """"""           """
"""""""""""""""""""""""""""""""""""""""""""""""""""

#config window size and color and title and whatever
root.title("Conway's Game of Life (reconstructed by Mark Anthony)")
root.geometry("500x500")
root.config(bg="white")

#defining functions



#making a lot of lines and shit
for i in range(55):
    canvas.create_line(-10, (i*10), 510, (i*10), width = 1)
    canvas.create_line((i*10), -10, (i*10), 500, width = 1)

canvas.pack()

root.mainloop()
