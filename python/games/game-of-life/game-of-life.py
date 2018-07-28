
import tkinter as tk
import numpy as np
import random as rand


window = tk.Tk()

sizeX = 401
sizeY = 401

canvas = tk.Canvas(window, width=sizeX, height=sizeY, bg='#bfffcf')

canvas.pack(padx=5, pady=5)

for i in range(1, sizeX + 1, 8):
    canvas.create_line(i, 1, i, sizeY + 1)

for j in range(1, sizeY + 1, 8):
    canvas.create_line(1, j, sizeX + 1, j)


class cell():

    def __init__(self, isAlive = False, nb_neighbors = 0):
        self.isAlive = isAlive
        self.nb_neighbors = nb_neighbors
        self.color = self.set_color()

    def next_state(self):
        if (self.nb_neighbors == 3 or (self.isAlive and self.nb_neighbors == 2)):
            self.isAlive = True
        else:
            self.isAlive = False
        self.set_color()

    def set_nb_neighbors(self, nb_neighbors):
        self.nb_neighbors = nb_neighbors

    def set_color(self):
        if (self.isAlive):
            self.color = 'blue'
        else:
            self.color = '#bfffff'


class GameOfLife():

    def __init__(self, canvas, sizeX=401, sizeY=401):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.map = np.zeros((self.sizeY // 8, self.sizeX // 8))
        self.neighbors = np.zeros((self.sizeY // 8, self.sizeX // 8))
        self.canvas = canvas
        self.canvas.bind('<B1-Motion>', self.get_creation)

    def map_refresh(self):
        for x in range(0,self.sizeX // 8):
            for y in range(0,self.sizeY // 8):
                self.set_cell_nb_neighbors(x, y)
        for x in range(0,self.sizeX // 8):
            for y in range(0,self.sizeY // 8):
                self.next_step(x, y)
                self.draw_cell(x, y)

    def next_step(self, x, y):
        if (self.neighbors[y, x] == 3  or (self.map[y, x] and self.neighbors[y, x] == 4)):
            self.map[y, x] = 1
        else:
            self.map[y, x] = 0

    def set_cell_alive(self, x, y):
        self.map[y, x] = 1
        self.draw_cell(x, y)

    def set_cell_dead(self, x, y):
        self.map[y, x] = 0
        self.draw_cell(x, y)

    def toggle_cell_state(self, x, y):
        if (self.map[y, x]):
            self.set_cell_dead(x, y)
        else:
            self.set_cell_alive(x, y)

    def set_cell_nb_neighbors(self, x, y):
        if (x == 0 and y == 0):
            self.neighbors[y, x] = self.map[y:y + 2, x: x + 2].sum()
        elif (x == (self.sizeX // 8) and y == 0):
            self.neighbors[y, x] = self.map[y:y + 2, x - 1: x + 1].sum()
        elif (x == 0 and y == (self.sizeY // 8)):
            self.neighbors[y, x] = self.map[y - 1:y + 1, x: x + 2].sum()
        elif (x == (self.sizeX // 8) and y == (self.sizeY // 8)):
            self.neighbors[y, x] = self.map[y - 1:y + 1, x - 1: x + 1].sum()
        elif (x == 0):
            self.neighbors[y, x] = self.map[y - 1:y + 2, x: x + 2].sum()
        elif (x == self.sizeX // 8):
            self.neighbors[y, x] = self.map[y - 1:y + 2, x - 1: x + 1].sum()
        elif (y == 0):
            self.neighbors[y, x] = self.map[y:y + 2, x - 1: x + 2].sum()
        elif (y == self.sizeY // 8):
            self.neighbors[y, x] = self.map[y - 1:y + 1, x - 1: x + 2].sum()
        else:
            self.neighbors[y, x] = self.map[y - 1:y + 2, x - 1: x + 2].sum()

    def set_random(self):
        for x in range(0,self.sizeX // 8):
            for y in range(0,self.sizeY // 8):
                self.map[y, x] = rand.randint(0,1)
                self.draw_cell(x, y)

    def draw_cell(self, x, y):
        list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        color = "#"
        for i in range(0,6):
            hexa = rand.choice(list)
            color = color + hexa

        if (self.map[y, x]):
            self.canvas.create_rectangle(x * 8 + 1, y * 8 + 1, x * 8 + 9, y * 8 + 9, fill=color)
        else:
            self.canvas.create_rectangle(x * 8 + 1, y * 8 + 1, x * 8 + 9, y * 8 + 9, fill='#bbffcc')

    def get_creation(self, event):
        x = event.x // 8
        y = event.y // 8
        print('{}, {}'.format(x, y))
        self.toggle_cell_state(x, y)



game = GameOfLife(canvas, sizeX, sizeY)

def play():
    game.map_refresh()

def rng():
    game.set_random()

button_quit = tk.Button(window, text='quit', command=window.quit)

button_quit.pack(padx=5, pady=5)

button_play = tk.Button(window, text='play', command=play)

button_play.pack(padx=5, pady=5)

button_rng = tk.Button(window, text='rand', command=rng)

button_rng.pack(padx=5, pady=5)

window.mainloop()
