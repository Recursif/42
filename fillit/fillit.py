

import tkinter as tk
import random as rand
import time

# Parseurs

def parse_sample(sample):
    list_tetriminos = []
    i = 0
    while (i < len(sample)):
        tetriminos = parse_tetriminos(i, sample)
        if (tetriminos):
            list_tetriminos.append(tetriminos)
            i += 20
        else:
            return (None)
        if (i >= len(sample) or sample[i] == '\n'):
            i += 1
        else:
            return (None)
    return (list_tetriminos)

def parse_tetriminos(n, sample):
    i = 0
    min_pos_x = 5
    min_pos_y = 5
    tetriminos = []
    nb_blocks = 0
    nb_lines = 0
    nb_chars = 0
    while (i < 20):
        if (sample[i + n] == '.'):
            nb_chars += 1
        elif (sample[i + n] == '#'):
            nb_chars += 1
            if (nb_blocks == 0 or sample[i + n - 1] == '#' or sample[i + n - 5] == '#' or (i < 19 and sample[i + n + 1])):
                tetriminos.append([nb_chars - 1, nb_lines])
                #print (tetriminos)
                if (nb_chars < min_pos_x):
                    min_pos_x = nb_chars - 1
                if (nb_blocks == 0):
                    min_pos_y = nb_lines
                nb_blocks += 1
            else:
                return (None)
        elif (sample[i + n] == '\n'):
            if (nb_chars == 4):
                nb_chars = 0
                nb_lines += 1
            else:
                return (None)
        else:
            return (None)
        i += 1

    for block in tetriminos:
        block[0] -= min_pos_x
        block[1] -= min_pos_y
    print (tetriminos)
    return (tetriminos)


def import_tetriminos(i):
    list_tetriminos = []
    with open('tetriminos/sample'+ str(i), 'r') as tetriminos:
        sample = tetriminos.read()
        list_tetriminos = parse_sample(sample)
        if (list_tetriminos):
            return (list_tetriminos)
        else:
            return (-1)

def init_square_size(n):
    i = 0
    while (i * i < 4 * n):
        i += 1
    return (i)

def init_pos(n):
    l = []
    i = 0
    while (i < n):
        l.append([0, 0])
        i += 1
    return (l)

def create_grid(n):
    grid = []
    i = 0
    while (i < n):
        row = []
        j = 0
        while (j < n):
            row.append('0')
            j += 1
        grid.append(row)
        i += 1
    return (grid)

def try_to_place(grid, l, pos):
    i = 0
    while (i < len(l)):
        x  = l[i][0] + pos[0]
        y  = l[i][1] + pos[1]
        if (x < len(grid) and y < len(grid[0]) and grid[y][x] == '0'):
            i += 1
        else:
            return (False)
    return (True)

def place(grid, l, pos, n):
    char = chr(ord('A') + n)
    i = 0
    while (i < len(l)):
        x  = l[i][0] + pos[0]
        y  = l[i][1] + pos[1]
        grid[y][x] = char
        i += 1
    print (grid)
    return (grid)

def unplace(grid, l, pos):
    i = 0
    while (i < len(l)):
        x  = l[i][0] + pos[0]
        y  = l[i][1] + pos[1]
        grid[y][x] = '0'
        i += 1
    return (grid)

def calculate_next_pos(pos, size):
    pos[0] += 1
    if (pos[0] >= size):
        pos[0] = 0
        pos[1] += 1
    if (pos[1] >= size):
        return (None)
    return (pos)


def fillit(l, canvas):
    square_size = init_square_size(len(l))
    l_pos = init_pos(len(l))
    grid = create_grid(square_size)
    i = 0
    while (i < len(l)):
        if (l_pos[i]):
            can_be_placed = try_to_place(grid, l[i], l_pos[i])
        else:
            can_be_placed = False
        if (can_be_placed):
            grid = place(grid, l[i], l_pos[i], i)
            print_grid(grid, canvas)
            i += 1
        else:
            next_pos = calculate_next_pos(l_pos[i], square_size)
            if (next_pos):
                l_pos[i] = next_pos
            else:
                if (i > 0):
                    l_pos[i] = [0, 0]
                    i -= 1
                    grid = unplace(grid, l[i], l_pos[i])
                    l_pos[i] = calculate_next_pos(l_pos[i], square_size)

                else:
                    square_size += 1
                    grid = create_grid(square_size)
                    l_pos[i] = [0, 0]
    return (grid)

def draw_grid(grid, canvas):
    i = 0
    while (i < len(grid)):
        j = 0
        while (j < len(grid[0])):
            draw_square(grid[i][j], j, i, canvas)
            j += 1
        i += 1

def draw_square(symb, x, y, canvas):
    nb = int(ord(symb) - ord('A'))
    canvas.create_rectangle(x * res + 2, y * res + 2, x * res + res + 2, y * res + res + 2, fill=color)

def print_grid(grid, canvas):
    i = 0
    while (i < len(grid)):
        print (grid[i])
        i += 1
    draw_grid(grid, canvas)
    time.sleep(1)

def create_list_color(n):
    list_color = []
    for i in range(n):
        list_color.append(choice_color())
    return (list_color)
    
def choice_color():
    list_hexa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    color = "#ee"
    for i in range(0,4):
        hexa = rand.choice(list_hexa)
        color = color + hexa
    return (color)


def create_canvas(cols, rows, res, window):
    sizeX = (res + 1) * cols + 1
    sizeY = (res + 1) * rows + 1

    canvas = tk.Canvas(window, width=sizeX, height=sizeY, bg='#bfffcf')

    canvas.pack(padx=5, pady=5)

    for i in range(3, sizeX + res, res):
        canvas.create_line(i, 0, i, sizeY + 3)

    for j in range(3, sizeY + res, res):
        canvas.create_line(0, j, sizeX + 3, j)
    
    return (canvas)



def main():
    
    window = tk.Tk()
    
    res = 10
    cols = 10
    rows = 10

    canvas = create_canvas(cols, rows, res, window)

    button_quit = tk.Button(window, text='quit', command=window.quit)
    
    button_quit.pack(padx=5, pady=5)

    l_tetriminos = import_tetriminos(2)

    print (l_tetriminos)

    l_color = create_list_color(len(l_tetriminos))

    print (l_color)

    grid = fillit(l_tetriminos, canvas)

    window.mainloop()

if __name__ == '__main__':
    main()
