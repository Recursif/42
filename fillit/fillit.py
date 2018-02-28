

import tkinter as tk
import random as rand


def import_tetriminos(i):
    with open('tetriminos/t'+ str(i) + '.txt', 'r') as tetriminos:
        return tetriminos.read()

def transform_tetriminos_list(t):
    i = 0
    j = 0
    size = 0
    l = []
    min = len(t)
    while (i < len(t)):
        if (t[i] == '\n'):
            if(j == 0):
                size = i + 1
            j += 1
            
        if (t[i] == '#'):
            l.append([i - j * size,j])
            if(min > i - j * size):
                min = i - j * size
        i += 1
    i = 0
    while (i < len(l)):
        l[i][0] -= min
        i += 1

    if (len(l) != 4):
        return 0;
    return l

t1 = import_tetriminos(5)

li = transform_tetriminos_list(t1)
print(t1)
print(li)
























"""
window = tk.Tk()

sizeX = 401
sizeY = 401

canvas = tk.Canvas(window, width=sizeX, height=sizeY, bg='#bfffcf')

canvas.pack(padx=5, pady=5)

for i in range(1, sizeX + 1, 8):
    canvas.create_line(i, 1, i, sizeY + 1)

for j in range(1, sizeY + 1, 8):
    canvas.create_line(1, j, sizeX + 1, j)


button_quit = tk.Button(window, text='quit', command=window.quit)

button_quit.pack(padx=5, pady=5)

window.mainloop()
"""
