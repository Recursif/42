

import tkinter as tk
import random as rand



def is_valid_sample(sample):
    i = 0
    nb_of_tetriminos = 0
    nb_of_line = 0
    nb_of_cube = 0
    last_cube = 0
    while (i < len(sample)):
        if (sample[i] != '.' and sample[i] != '#' and sample != '\n'):
            return (0)
        if (sample[i] ==  '#'):
            nb_of_cube += 1
            diff = i - last_cube
            if (diff != i and diff != 5 and diff != 1):
                return (0)
        if (sample[i] == '\n'):
            if (nb_of_line == 4):



def char_counter(char, sample):
    res = 0
    i = 0
    while (i < len(sample)):
        if (sample[i] == char):
            res += 1
        i += 1
    return (res)

def import_tetriminos(i):
    with open('tetriminos/sample'+ str(i), 'r') as tetriminos:
        sample = tetriminos.read()
        if (is_valid-sample(sample)):
            return (sample)
        else:
            return (-1)

def sample_to_list(sample):
    tetriminos = []
    



    return (tetrinminos)

    
sample = import_tetriminos(1)

li = transform_tetriminos_list(t1)
print(t1)
print(li)

window = tk.Tk()


res = 10
cols = 10
rows = 10

sizeX = res * cols
sizeY = res * rows

canvas = tk.Canvas(window, width=sizeX, height=sizeY, bg='#bfffcf')

canvas.pack(padx=5, pady=5)

for i in range(0, sizeX, res):
    canvas.create_line(i, 0, i, sizeY)

for j in range(0, sizeY, res):
    canvas.create_line(0, j, sizeX, j)

list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
color = "#"
for i in range(0,6):
    hexa = rand.choice(list)
    color = color + hexa

for cube in li:
    canvas.create_rectangle(cube[0] * res, cube[1] * res, cube[0] * res + res, cube[1] * res + res, fill=color)



button_quit = tk.Button(window, text='quit', command=window.quit)

button_quit.pack(padx=5, pady=5)

window.mainloop()
canvas.create_line(i, 1, i, sizeY + 1)
