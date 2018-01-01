

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


class Fillit(object):
    """Object to fillit.

    Parameters
    -----------
    pieces : list of t_str
        set of tetriminos to fillit.

    size : 2-uplet
        size of the grid to fill.

    """

    def __init__(self, pieces, size):
        self.pieces = pieces
        self.size = size

    def fillit(self):
        """Function that fit the piecse in the grid

class Tetriminos(object):
    """Objet tetriminos.

    Parameters
    ----------
    t_str : string
        String representing the tetriminos.

    authorized_char : 2-uplet
        Character authorized.

    size : 2-uplet
        Size of the tetriminos.

    Attribute
    ----------
    pattern : 2d-array
        2d-array representing the tetriminos.

    """

    def __init__(self, t_str, authorized_char=('0','#') , size=(4, 4)):
        self.t_str = t_str
        self.authorized_char = authorized_char
        self.size = size
        self.pattern = []
        if (self.is_valid_tetriminos()):
            self.convert_to_pattern()


    def convert_to_pattern(self):
        """Convert the t_str in a 2d-array"""
        for j in range(0, self.size[1] - 1):
            for i in range(0, self.size[0] - 1)
                pattern[j].append(t_str[i + j * (self.size[0] + 1)])


    def is_valid_tetriminos(self):
        """Check if the t_str represent a valid tetriminos"""
        rows = 0
        cols = 0
        for i in range(len(t_str)):
            if (i == authorized_char[0] || i == authorized_char[1]):
                cols += 1
            elif (i == '\n'):
                if (!(cols == size[0])):
                    print("Wrong number of column!")
                    return (0)
                rows += 1
                cols = 0
            else :
                print("Unauthorized character!")
                return (0)
        if ((cols, rows) == size)
            return (1)
        else :
            print("Bad size!")
            return (0)
