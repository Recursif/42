

import tkinter as tk
from Tetriminos import *

with open('Tetriminos/t1', 'r') as tfile:
    t_str = tfile.read()

T1 = Tetriminos(t_str)

print(T1.pattern)
