

from Table import *

class Tetriminos(object):
    """Object tetriminos.

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

    def __init__(self, t_str, authorized_char=('0','#') , size=[4, 4]):
        self.t_str = t_str
        self.authorized_char = authorized_char
        self.size = size
        self.pattern = []
        if (self.is_valid_tetriminos()):
            self.convert_to_pattern()
            self.reduce_size()

    def convert_to_pattern(self):
        """Convert the t_str in a 2d-array."""
        for j in range(self.size[1]):
            self.pattern.append([])
            for i in range(self.size[0]):
                self.pattern[j].append(1 if (self.t_str[i + j * (self.size[0] + 1)] == self.authorized_char[1]) else 0)

    def remove_row(self, n_row):
        """Remove the column n_row."""
        tmp = self.pattern
        self.pattern = self.pattern[:n_row]
        self.pattern.extend(tmp[n_row + 1:])

    def remove_col(self, n_col):
        """Remove the column n_col."""
        for i in range(len(self.pattern)):
            tmp = self.pattern[i]
            self.pattern[i] = self.pattern[i][:col]
            self.pattern[i].extend(self.pattern[i][col + 1:])

    def reduce_size(self):
        """Reduce the tetriminos to its minimun size."""
        x = 0
        while (x < self.size[0]):
            if (not(sum(self.pattern[x]))):
                self.remove_row(x)
                print(self.pattern)
                self.size[0] -= 1
                x = 0
            x += 1

        tmp = 0
        y = 0
        while (y < self.size[1]):
            print(y, self.size[1], self.size[0])
            for i in range(self.size[0]):
                if (self.size[0] == 1):
                    break
                if (self.pattern[i][y]):
                    tmp += 1
            print(self.pattern)
            if (tmp):
                self.remove_row(y)
                self.size[1] -= 1
                y = 0
            y += 1
            tmp = 0

    def is_cube_have_a_neighbors(self, x, y):
        """Check if the cube at position (x , y) have a neighbors."""
        X = [x - 1, x + 1, x, x]
        Y = [y, y, y - 1, y + 1]
        for i, j in zip(X, Y):
            if (0 <= i and 0 <= j and i < self.size[0] and j < self.size[1]):
                if (self.t_str[i + self.size[0] * j] == self.authorized_char[1]):
                    return (1)
        return (0)

    def is_valid_tetriminos(self):
        """Check if the t_str represent a valid tetriminos."""
        row = 0
        col = 0
        nb_cube = 0
        for i in range(len(self.t_str) - 1):
            if (self.t_str[i] == self.authorized_char[0]):
                col += 1
            elif (self.t_str[i] == self.authorized_char[1]):
                if (not(self.is_cube_have_a_neighbors(i - row * self.size[0], row))):
                    print("Invalid tetriminos!!")
                    return (0)
                nb_cube += 1
                col += 1
            elif (self.t_str[i] == '\n'):
                if (not(col == self.size[0])):
                    print("Wrong number of column!")
                    return (0)
                row += 1
                col = 0
            else :
                print("Unauthorized character!")
                return (0)
        if (row in self.size and nb_cube == 4):
            return (1)
        elif (nb_cube != 4):
            print("Not a tetriminos!")
            return (0)
        else :
            print("Wrong number of row!")
            return (0)
